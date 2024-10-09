import pandas as pd
import logging

# Set up logging for the ETL process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(file_path):
    """Extract data from CSV file."""
    try:
        logging.info("Extracting data from CSV file.")
        df = pd.read_csv(file_path, low_memory=False)
        logging.info(f"Data extraction complete. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except Exception as e:
        logging.error(f"Error during data extraction: {e}")
        raise

def transform_data(df):
    """Transform the data by filtering and processing."""
    logging.info("Starting data transformation.")

    # Define the target columns to be used in the analysis
    target_columns = ['PatientID',
                      'StudyInstanceUID',
                      'SeriesInstanceUID',
                      'StudyDescription',
                      'SeriesDescription',
                      'PixelSpacing',
                      'SliceThickness',
                      'ConvolutionKernel',
                      'ImageOrientationPatient',
                      'Modality']

    # Filter DataFrame to include only the target columns and remove columns with more than 30% missing values
    threshold = int(df.shape[0] * 0.3)
    df = df[target_columns].dropna(axis=1, thresh=threshold)

    # Filter for rows where the modality is 'CT'
    df = df[df.Modality == 'CT']

    # Function to check if the ImageOrientationPatient values are within a tolerance of the target
    def tolerance(value, target, tolerance=0.15):
        if pd.isna(value):
            return False
        components = list(map(float, str(value).split('\\')))
        target_components = list(map(float, target.split('\\')))
        return all(abs(comp - tgt) <= tolerance for comp, tgt in zip(components, target_components))

    # Target orientation to compare against
    target_orientation = '1\\0\\0\\0\\1\\0'
    df = df[df.ImageOrientationPatient.apply(lambda x: tolerance(x, target_orientation))]

    # Filter rows where Slice Thickness is between 2.5 and 5 mm
    df = df[(df.SliceThickness >= 2.5) & (df.SliceThickness <= 5)]

    # Filter SeriesDescription to include only rows with 'head' or 'brain'
    df = df[df.SeriesDescription.str.contains('head|brain', case=False, na=False)]

    # Filter StudyDescription to exclude rows with 'CTA HEAD' or 'Angio'
    df = df[~df.StudyDescription.str.contains('angio|CTA HEAD', case=False, na=False)]

    # Function to filter PixelSpacing values
    def filter_pixel_spacing(value):
        try:
            val1, val2 = map(float, value.split('\\'))
        except (ValueError, AttributeError):
            return False
        return val1 <= 0.55 and val2 <= 0.55

    # Apply PixelSpacing filter
    df = df[df.PixelSpacing.apply(filter_pixel_spacing)]

    logging.info(f"Data transformation complete. Rows after transformation: {df.shape[0]}")
    return df

def load_data(df, output_file):
    """Load transformed data to a CSV file."""
    try:
        logging.info(f"Loading data to {output_file}.")
        df.to_csv(output_file, index=False)
        logging.info("Data loading complete.")
    except Exception as e:
        logging.error(f"Error during data loading: {e}")
        raise

def main():
    """Main ETL function to orchestrate the process."""
    input_file = 'data/part1_inventory_test.csv'
    output_file = 'data/transformed_inventory_data.csv'
    
    # Extract, Transform, Load process
    try:
        df = extract_data(input_file)
        transformed_df = transform_data(df)
        load_data(transformed_df, output_file)
    except Exception as e:
        logging.error(f"ETL process failed: {e}")

if __name__ == "__main__":
    main()
