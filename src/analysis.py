import pandas as pd

print("🚀 Analysis Started")

# Load processed data
df = pd.read_csv("data/processed_data.csv")

print("✅ Data Loaded")
print(df.head())

# -------------------------------
# Route Level Analysis
# -------------------------------

route_analysis = df.groupby('Route').agg({
    'Lead Time': ['mean', 'count', 'std']
}).reset_index()

# Rename columns
route_analysis.columns = ['Route', 'Avg Lead Time', 'Total Orders', 'Variability']

print("\n📊 Route Analysis Preview:")
print(route_analysis.head())

# -------------------------------
# Top 10 Efficient Routes
# -------------------------------
top_routes = route_analysis.sort_values('Avg Lead Time').head(10)

print("\n🔥 Top 10 Fastest Routes:")
print(top_routes)

# -------------------------------
# Bottom 10 Inefficient Routes
# -------------------------------
worst_routes = route_analysis.sort_values('Avg Lead Time', ascending=False).head(10)

print("\n🚨 Top 10 Slowest Routes:")
print(worst_routes)

# -------------------------------
# Save results
# -------------------------------
route_analysis.to_csv("data/route_analysis.csv", index=False)

print("\n✅ Analysis Completed!")