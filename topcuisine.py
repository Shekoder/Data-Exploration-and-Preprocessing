import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Update this path with the correct path to your file
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Calculate basic statistical measures for numerical columns
print('Basic Statistical Measures for Numerical Columns:')
print(df.describe())

# Explore the distribution of categorical variables
categorical_columns = ['Country Code', 'City', 'Cuisines']

for col in categorical_columns:
    print(f'\nDistribution of {col}:')
    print(df[col].value_counts())

    # Plot the distribution with larger figure size and more space between bars
    plt.figure(figsize=(18, 10))  # Increase figure size for more space
    ax = sns.countplot(data=df, x=col, order=df[col].value_counts().index, dodge=False, width=0.5)  # Adjust bar width
    
    # Select 5 evenly spaced tick locations and labels
    x_ticks = list(range(0, len(df[col].value_counts()), max(1, len(df[col].value_counts()) // 5)))
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([df[col].value_counts().index[i] for i in x_ticks], rotation=45, ha='right', fontsize=14)

    # Increase space between x-axis labels
    ax.tick_params(axis='x', which='major', pad=20)  # Increase padding between ticks and labels
    
    plt.title(f'Distribution of {col}', fontsize=16)  # Set title font size
    plt.xlabel(col, fontsize=14)  # Set font size for the x-axis label
    plt.ylabel('Frequency', fontsize=14)  # Set font size for the y-axis label
    plt.tight_layout()  # Adjust layout to fit everything nicely
    plt.show()

# Identify the top cuisines with the highest number of restaurants
# Split 'Cuisines' into individual cuisines
df['Cuisines'] = df['Cuisines'].astype(str)  # Ensure that Cuisines is a string
cuisines_series = df['Cuisines'].str.split(', ', expand=True).stack()
top_cuisines = cuisines_series.value_counts()

print('\nTop Cuisines with the Highest Number of Restaurants:')
print(top_cuisines)

# Identify the top cities with the highest number of restaurants
top_cities = df['City'].value_counts()

print('\nTop Cities with the Highest Number of Restaurants:')
print(top_cities)
