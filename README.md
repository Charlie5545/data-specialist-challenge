# data-specialist-methinks-challenge
Data Specialist - Methinks Challenge

# Cleaning and Inventory task 1

Analysis and Filter criteria analyzed on 'Carlos_Gil_Data_Specialist_Methinks_Challenge.ipynb'
ETL script on 'etl_process.py'

## Workflow for Cleaning and Inventory

1. **Filter by Modality**:  
   Keep only rows where `df.Modality == 'CT'`.

2. **Image Orientation Patient**:  
   Apply tolerance to `ImageOrientationPatient` values of `'1\\0\\0\\0\\1\\0'` with a tolerance of **0.15 mm**.

3. **Slice Thickness**:  
   Filter for rows where `2.5 <= SliceThickness <= 5 mm`.

4. **Series Description**:  
   Keep rows where `SeriesDescription` contains 'head' or 'brain' (case insensitive).

5. **Study Description**:  
   Include rows where `StudyDescription` contains 'angio' or 'CTA HEAD' (case insensitive).

6. **Pixel Spacing**:  
   Filter for rows where `PixelSpacing <= 0.55`.

## Instructions to use ETL script
To use ETL 
1. Make sure you have the required CSV files in your data/ directory (or adjust the file paths accordingly).
2. Navigate to the directory where you saved the .py file.
3. Run 'python etl_process.py'

The script will extract, transform, and load the data, logging each step and saving the transformed data to transformed_inventory_data.csv

# Analysis task 2

Analysis and Filter criteria analyzed on 'Carlos_Gil_Data_Specialist_Methinks_Challenge.ipynb'
