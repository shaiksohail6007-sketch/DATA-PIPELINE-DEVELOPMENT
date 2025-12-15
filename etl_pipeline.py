import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# EXTRACT
def extract_data(path):
    print("🔹 Extracting data...")
    df = pd.read_csv(path)
    return df

# TRANSFORM
def transform_data(df):
    print("🔹 Cleaning & Transforming data...")

    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))

    # Encode categorical columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    # Feature scaling
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df

#  LOAD
def load_data(df, output_path):
    print("🔹 Loading final processed file...")
    df.to_csv(output_path, index=False)
    print(f"✅ File saved as: {output_path}")

#  MAIN PIPELINE FUNCTION
def run_pipeline():
    input_file = "input_data.csv"
    output_file = "processed_data.csv"

    df_raw = extract_data(input_file)
    df_cleaned = transform_data(df_raw)
    load_data(df_cleaned, output_file)

    print("🎉 ETL Pipeline Completed Successfully!")

# Run the Pipeline
run_pipeline()

