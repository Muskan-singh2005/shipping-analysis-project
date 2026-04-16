
import pandas as pd

# Load dataset
df = pd.read_csv("data/Nassau Candy Distributor.csv")

# Show first few rows (for checking)
print(df.head())

# Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

# Create Lead Time (in days)
df['Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days

# Remove invalid lead times (negative values)
df = df[df['Lead Time'] >= 0]

# Drop missing values
df = df.dropna()

# Standardize column names (optional but good practice)
df.columns = df.columns.str.strip()

# Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("✅ Data cleaning completed successfully!")