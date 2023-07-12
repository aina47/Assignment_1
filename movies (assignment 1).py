#!/usr/bin/env python
# coding: utf-8

# In[49]:


#import all necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import geopandas as gpd


# In[50]:


# Read the CSV file into a DataFrame
df = pd.read_csv('movies.csv')

# Descriptive Statistics
print(df.describe())  # Basic statistics of numerical columns

df


# # Describing Data

# In[51]:


#there are 3169 rows and 15 columns in the data set
print ("Dataset shape: ", df.shape) 


# In[52]:


print(df.head()) #list out 5 head datas


# In[53]:


#Name of the columns
print(df.columns.values)


# In[54]:


# non null count and data types of the dataset.
df.info()


# In[55]:


#Count the number of row/cell that contain NaN for the entire dataframe
result = df.isnull().sum()

result


# In[56]:


# missing data in the dataset
msno.matrix(df)


# # Editing Data

# In[57]:


# Delete / Eliminate year from 1980 until 1999
# Convert 'year' column to numeric data type
df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Filter out the rows with years between 1980 and 1999
df = df[(df['year'] < 1980) | (df['year'] > 1999)]

# Verify the changes
print(df['year'])


# In[58]:


#list of movies with score 7 and above
# Filter out the rows with rating 7 or above
high_rated_movies = df[df['score'] >= 7]

# Print the list of movies with rating 7 or above
print(high_rated_movies[['name', 'score']])


# In[59]:


#Delete/Eliminate the null value
# Drop rows with null values
df = df.dropna()

# Verify the changes
print (df.head())


# # Visualizing Data

# In[60]:


#Total movies from each country
country_counts = df['country'].value_counts()
print(country_counts)  


# In[61]:


#Does my data have a spatial or geographic component?
#Yes, spatial or geographic component:

# Read country shapefile
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Group by country and count movies
movies_by_country = df.groupby('country').size().reset_index(name='movie_count')

# Merge movie count with country shapefile
world = world.merge(movies_by_country, left_on='name', right_on='country', how='left')

# Plot choropleth map
world.plot(column='movie_count', cmap='Blues', linewidth=0.8, edgecolor='0.8', legend=True)
plt.title('Movie Distribution by Country')
plt.show()


# In[62]:


#Does my data have a temporal component, showing change over time?
#Yes, released movies group by year and count movies

year_counts = df['year'].value_counts().sort_index()
print(year_counts)
movies_by_year = df.groupby('year').size()

# Plot line chart
movies_by_year.plot(kind='line', marker='o')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.title('Number of Movies Released Over Time')
plt.grid(True)
plt.show()


# In[63]:


#list of movies with score 7 and above
# Filter out the rows with rating 7 or above
high_rated_movies = df[df['score'] >= 7]

# Print the list of movies with rating 7 or above
print(high_rated_movies[['name', 'score']])


# In[64]:


# Value counts of the rating column
rating_counts = df['rating'].value_counts()
print(rating_counts)
# the highest total of movies are in R rating


# In[65]:


# Plotting genre distribution
rating_counts.plot(kind='bar')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Genre Distribution')
plt.show()


# In[66]:


# How many variables am I trying to represent?
# At here, we show correlation between ratings and gross revenue of the movies
# Plot scatter plot
plt.scatter(df['rating'], df['gross'], alpha=0.5)
plt.xlabel('Rating')
plt.ylabel('Gross Revenue')
plt.title('Rating vs. Gross Revenue')
plt.show()


# In[67]:


# Who is the audience I am trying to reach?
# General audience

# Count movies based on movie genres
genre_counts = df['genre'].value_counts()
print(genre_counts)

# Plotting genre distribution
genre_counts.plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Genre Distribution')
plt.show()

# Pie chart for genre distribution
genre_counts = df['genre'].value_counts()
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title('Genre Distribution')
plt.show()


# In[68]:


# Who is the audience I am trying to reach?
# Movie Enthusiast
# Scatter plot of rating vs. gross revenue
sns.scatterplot(data=df, x='rating', y='gross', hue='genre')
plt.title('Rating vs. Gross Revenue by Genre')
plt.xlabel('Rating')
plt.ylabel('Gross Revenue')
plt.show()


# In[69]:


# General Audience
# Bar plot of average rating by year
average_rating_by_year = df.groupby('year')['score'].mean().reset_index()
sns.barplot(data=average_rating_by_year, x='year', y='score')
plt.title('Average Score by Year')
plt.xlabel('Year')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.show()


# In[70]:


msno.matrix(df) #this is because there are no null values


# In[71]:


# Director and Writer Analysis
# Top 10 directors
director_counts = df['director'].value_counts()
print(director_counts.head(10))  


# In[72]:


writer_counts = df['writer'].value_counts()
print(writer_counts.head(10))  # Top 10 writers


# In[73]:


# Movie Budget and Gross
total_budget = df['budget'].sum()
print(f"Total Budget: ${total_budget}")

total_gross = df['gross'].sum()
print(f"Total Gross: ${total_gross}")


# In[74]:


# Country and Company Analysis
country_counts = df['country'].value_counts()
print(country_counts.head(10))  # Top 10 countries

company_counts = df['company'].value_counts()
print(company_counts.head(10))  # Top 10 production companies

# Highest Score Movies
top_rated_movies = df.nlargest(10, 'score')  # Get top 10 rated/score movies
print(top_rated_movies[['name', 'score', 'genre', 'year']])


# In[75]:


# Top 10 directors with most movies
popular_directors = df['director'].value_counts().head(10)  
print(popular_directors)

# Top 10 writers with most movies
writer_counts = df['writer'].value_counts()
print(writer_counts.head(10))  


# In[ ]:




