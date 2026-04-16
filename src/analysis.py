import pandas as pd

print("🚀 Analysis Started")

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_csv("data/processed_data.csv")

print("✅ Data Loaded")
print(df.head())

print("\n📌 Columns in dataset:")
print(df.columns)

# -------------------------------
# Route Analysis
# -------------------------------
route_analysis = df.groupby('Route').agg({
    'Lead Time': ['mean', 'count', 'std']
}).reset_index()

route_analysis.columns = ['Route', 'Avg Lead Time', 'Total Orders', 'Variability']

print("\n📊 Route Analysis Preview:")
print(route_analysis.head())

# Top 10 fastest routes
top_routes = route_analysis.sort_values('Avg Lead Time').head(10)
print("\n🔥 Top 10 Fastest Routes:")
print(top_routes)

# Bottom 10 slowest routes
worst_routes = route_analysis.sort_values('Avg Lead Time', ascending=False).head(10)
print("\n🚨 Top 10 Slowest Routes:")
print(worst_routes)

# Save results
route_analysis.to_csv("data/route_analysis.csv", index=False)

print("\n✅ Analysis Completed!")

# -------------------------------
# Create Target Column (Delayed)
# -------------------------------
threshold = df['Lead Time'].mean()

df['Delayed'] = df['Lead Time'].apply(lambda x: 1 if x > threshold else 0)

print("\n✅ Target column 'Delayed' created")

# -------------------------------
# Machine Learning Model
# -------------------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score

print("\n🤖 ML Model Started")

df_ml = df.copy()

# Convert categorical columns to numeric
le = LabelEncoder()
for col in df_ml.select_dtypes(include='object').columns:
    df_ml[col] = le.fit_transform(df_ml[col])

# Define features & target
target_column = 'Delayed'

X = df_ml.drop(target_column, axis=1)
y = df_ml[target_column]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = KNeighborsClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n📊 Model Results:")
print(f"Accuracy: {accuracy:.2f}")
print(f"F1 Score: {f1:.2f}")

print("\n✅ ML Model Completed")