
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Step 1: Extract - Load the data
df = pd.read_csv("data.csv")
print("Original Data:")
print(df)

# Step 2: Transform - Clean and preprocess
# Remove rows with missing values
df_clean = df.dropna()

# Scale numeric columns
scaler = StandardScaler()
numeric_cols = df_clean.select_dtypes(include='number').columns
df_clean[numeric_cols] = scaler.fit_transform(df_clean[numeric_cols])

# Step 3: Load - Save the cleaned data
df_clean.to_csv("cleaned_data.csv", index=False)
print("ETL process complete. Cleaned data saved to cleaned_data.csv")
