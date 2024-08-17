import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Update this path with the correct path to your file
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'

# Load the dataset
df = pd.read_csv( r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv')

# Calculate basic statistical measures for numerical columns
print('Basic Statistical Measures for Numerical Columns:')
print(df.describe())

# Explore the distribution of categorical variables
categorical_columns = ['Country Code', 'City', 'Cuisines']

for col in categorical_columns:
    print(f'\nDistribution of {col}:')
    print(df[col].value_counts())

    # Plot the distribution with a smaller figure size
    plt.figure(figsize=(10, 6))  # Smaller figure size
    ax = sns.countplot(data=df, x=col, order=df[col].value_counts().index, dodge=False, width=0.5)  # Adjust bar width
    
    # Limit x-axis labels to show only 5 ticks
    ax.xaxis.set_major_locator(ticker.MaxNLocator(5))

    # Full names of x-axis labels with rotation for readability
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)

    # Increase space between x-axis labels
    ax.tick_params(axis='x', pad=15)  # Adjust padding between ticks and labels
    
    plt.title(f'Distribution of {col}', fontsize=14)  # Adjust title font size
    plt.xlabel(col, fontsize=12)  # Adjust font size for the x-axis label
    plt.ylabel('Frequency', fontsize=12)  # Adjust font size for the y-axis label
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
