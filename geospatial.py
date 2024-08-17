import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'
df = pd.read_csv(r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv')


# 1. Visualize the locations of restaurants on a map
# Initialize a map centered around the mean latitude and longitude
restaurant_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=12)

# Add points to the map
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name'],
    ).add_to(restaurant_map)


# 2. Analyze the distribution of restaurants across different cities or countries

# Distribution by city
plt.figure(figsize=(24, 12))
city_counts = df['City'].value_counts().head(20)  # Display top 20 cities
sns.barplot(y=city_counts.index, x=city_counts.values)
plt.title('Top 20 Cities with the Highest Number of Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('City')
plt.show()

# Distribution by country
plt.figure(figsize=(16, 8))
country_counts = df['Country Code'].value_counts().head(10)  # Display top 10 countries
sns.barplot(y=country_counts.index, x=country_counts.values)
plt.title('Top 10 Countries with the Highest Number of Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('Country Code')
plt.show()

# 3. Correlation between restaurant's location and its rating

# Correlation matrix
correlation_matrix = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()
print('Correlation matrix:')
print(correlation_matrix)

# Visualize correlation using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Longitude', y='Latitude', hue='Aggregate rating', data=df, palette='coolwarm', size='Aggregate rating', sizes=(20, 200))
plt.title('Restaurant Locations Colored by Aggregate Rating')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
