import pandas as pd

# Load CSV file
df = pd.read_csv("quotes.csv")

# Remove leading/trailing spaces
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned data to a new CSV file
df.to_csv("quotes_cleaned.csv", index=False)

print("Data cleaned and saved as quotes_cleaned.csv")
