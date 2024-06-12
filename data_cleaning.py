import pandas as pd

def clean_data(file_path):
    print("Cleaning data .. (0%)")

    # Load the dataset
    df = pd.read_csv(file_path)
    print("Cleaning data .. (10%)")

    # Handle missing values
    df['Electric Range'].fillna(df['Electric Range'].mean(), inplace=True)
    df['Base MSRP'].fillna(df['Base MSRP'].mean(), inplace=True)
    print("Cleaning data .. (30%)")

    # Fill missing values for categorical data with 'Unknown'
    categorical_columns = ['Country', 'City', 'State', 'Postal Code', 'Make', 'Model', 'Electric Vehicle Type', 
                           'Clean Alternative Fuel Vehicle (CAFV) Eligibility', 'Legislative District', 'Electric Utility', '2020 Census Tract']
    for column in categorical_columns:
        df[column].fillna('Unknown', inplace=True)
    print("Cleaning data .. (60%)")

    # Drop duplicates based on VIN as it's a unique identifier for vehicles
    df.drop_duplicates(subset='VIN (1-10)', inplace=True)
    print("Cleaning data .. (80%)")

    # Ensure correct data types
    df['Model Year'] = df['Model Year'].astype(int)
    df['Electric Range'] = df['Electric Range'].astype(float)
    df['Base MSRP'] = df['Base MSRP'].astype(float)
    print("Cleaning data .. (100%)")
    print(" ---------- Data Cleaning Completed ----------")
    print()

    return df