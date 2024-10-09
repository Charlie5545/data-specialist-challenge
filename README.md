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

## ETL Output

The ETl script generates 'transformed_inventory_data.csv', here a summary:

Total number of patients: 305

<class 'pandas.core.frame.DataFrame'>
Int64Index: 699 entries, 1 to 8407
Data columns (total 10 columns):
 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   PatientID                699 non-null    object 
 1   StudyInstanceUID         699 non-null    object 
 2   SeriesInstanceUID        699 non-null    object 
 3   StudyDescription         699 non-null    object 
 4   SeriesDescription        699 non-null    object 
 5   PixelSpacing             699 non-null    object 
 6   SliceThickness           699 non-null    float64
 7   ConvolutionKernel        691 non-null    object 
 8   ImageOrientationPatient  699 non-null    object 
 9   Modality                 699 non-null    object 
dtypes: float64(1), object(9)
memory usage: 60.1+ KB

logging information example:

2024-10-09 19:50:04,696 - INFO - Extracting data from CSV file.
2024-10-09 19:50:04,836 - INFO - Data extraction complete. Rows: 8454, Columns: 206
2024-10-09 19:50:04,837 - INFO - Starting data transformation.
2024-10-09 19:50:04,874 - INFO - Data transformation complete. Rows after transformation: 699
2024-10-09 19:50:04,875 - INFO - Loading data to data/transformed_inventory_data.csv.
2024-10-09 19:50:04,882 - INFO - Data loading complete.

## Instructions to use ETL script
To use ETL 
1. Make sure you have the required CSV files in your data/ directory (or adjust the file paths accordingly).
2. Navigate to the directory where you saved the .py file.
3. Run 'python etl_process.py'

The script will extract, transform, and load the data, logging each step and saving the transformed data to transformed_inventory_data.csv

# Analysis task 2

Analysis and Filter criteria analyzed on 'Carlos_Gil_Data_Specialist_Methinks_Challenge.ipynb'

1. Compute AUROC for Model_1 and Model_2, and select the one with the higher AUROC 

Best model: Model_1, 
AUROC Model_1: 0.5096153846153846 
AUROC Model_2: 0.34134615384615385 

2. Compute sensitivity and specificity for thresholds [0.3, 0.5, 0.7, 0.9] 

Threshold: 0.3, Sensitivity: 0.67, Specificity: 0.42
Threshold: 0.5, Sensitivity: 0.42, Specificity: 0.54
Threshold: 0.7, Sensitivity: 0.25, Specificity: 0.81
Threshold: 0.9, Sensitivity: 0.12, Specificity: 0.92
Selected threshold: 0.7 

3. Select False Positive patients with the selected threshold 

False Positive patients: ['X99', 'G30', 'K91', 'E139', 'G66']

4. Compute the image histogram. You should see that two patients have something weird in the histogram, identify them.

![image](https://github.com/user-attachments/assets/3beeac15-c334-4927-8999-9ec6ffe9c035)
Patients with abnormal Histogram are E139 and G30.

5. Visualize the masked images for abnormal patients

![image](https://github.com/user-attachments/assets/7faa40f6-4966-4701-923e-6eacc0a12115)
Analysis for Patient E139:
Scan is not valid as there is no information for half of the image

![image](https://github.com/user-attachments/assets/e2f29ed0-6a4a-43c4-973d-bfd81aa6b95a)
Analysis for Patient G30:
The scan is fine but the pixel intensity is too bright - over the range - so needs to be modified
