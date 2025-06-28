import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Fill missing values in 'director', 'cast', and 'country' with "Unknown"
df.fillna({
    'director': 'Unknown',
    'cast': 'Unknown',
    'country': 'Unknown'
}, inplace=True)

# For 'date_added' and 'rating', let's drop the few rows that have missing values
df.dropna(subset=['date_added', 'rating'], inplace=True)

# Verify that the missing values have been handled
print(df.isnull().sum())

# Check for duplicate rows
print(f"Number of duplicate rows: {df.duplicated().sum()}")

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Verify that duplicates have been removed
print(f"Number of duplicate rows after removal: {df.duplicated().sum()}")

# Strip whitespace and then convert to datetime
df['date_added'] = pd.to_datetime(df['date_added'].str.strip())

# You can also format it to 'dd-mm-yyyy' if you want a specific string format
# df['date_added_formatted'] = df['date_added'].dt.strftime('%d-%m-%Y')

# Display the data type of the 'date_added' column to verify
print(df.info())

# Save the cleaned dataframe to a new CSV file
df.to_csv('netflix_titles_cleaned.csv', index=False)