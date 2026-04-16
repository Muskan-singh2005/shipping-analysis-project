
import pandas as pd

print("🚀 Feature Engineering Started")

# Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# -------------------------------
# Step 1: Map Product → Factory
# -------------------------------

factory_map = {
    "Wonka Bar - Nutty Crunch Surprise": "Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows": "Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious": "Lot's O' Nuts",
    "Wonka Bar - Milk Chocolate": "Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel": "Wicked Choccy's",
    "Laffy Taffy": "Sugar Shack",
    "SweeTARTS": "Sugar Shack",
    "Nerds": "Sugar Shack",
    "Fun Dip": "Sugar Shack",
    "Fizzy Lifting Drinks": "Sugar Shack",
    "Everlasting Gobstopper": "Secret Factory",
    "Hair Toffee": "The Other Factory",
    "Lickable Wallpaper": "Secret Factory",
    "Wonka Gum": "Secret Factory",
    "Kazookles": "The Other Factory"
}

df['Factory'] = df['Product Name'].map(factory_map)

# -------------------------------
# Step 2: Create Route
# -------------------------------

df['Route'] = df['Factory'] + " -> " + df['State/Province']

# -------------------------------
# Step 3: Save processed data
# -------------------------------

df.to_csv("data/processed_data.csv", index=False)

print("✅ Feature Engineering Completed!")