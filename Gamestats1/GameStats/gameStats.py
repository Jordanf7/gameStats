'''
Created on Dec 10, 2023

@author: Jordan
'''
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


# Read CSV file into a DataFrame
gamestats = pd.read_csv('C:/Users/Jorda/Downloads/Cleaned Data 2.csv')

print(gamestats.columns)
print(gamestats.shape)
print(gamestats.isnull().sum())

cleaned_gamestats = gamestats[~gamestats.isnull().any(axis=1)].reset_index().drop(columns=['index'])
cleaned_gamestats 
cleaned_gamestats.drop(columns=['Rating', 'User_Count'], inplace=True)
print(cleaned_gamestats.Genre.value_counts())

print(cleaned_gamestats.Developer.value_counts())

#genre pie
genre_counts = cleaned_gamestats['Genre'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Genres')
plt.show()

#dev pie
developer_counts = cleaned_gamestats['Developer'].value_counts()
frequent_developers = developer_counts[developer_counts >= 57].index
cleaned_gamestats = cleaned_gamestats[cleaned_gamestats['Developer'].isin(frequent_developers)].reset_index(drop=True)

cleaned_gamestats['Developer'] = np.where(cleaned_gamestats['Developer'].str.startswith('E'),
                                          'EA', cleaned_gamestats['Developer'])

developer_counts = cleaned_gamestats['Developer'].value_counts()

#top 11 devs
plt.figure(figsize=(10, 10))
plt.pie(developer_counts, labels=developer_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of top 11 Developers')
plt.show()


#global sales by genre
average_sales =cleaned_gamestats['Global_Sales'].value_counts()
average_sales_by_genre = cleaned_gamestats.groupby('Genre')['Global_Sales'].mean()

plt.figure(figsize=(12, 6))
average_sales_by_genre.sort_values().plot(kind='bar', color='green')
plt.ylabel('Average Sales')
plt.xlabel('Genre')
plt.title('Average Global Sales by Genre')
plt.xticks(rotation = 360)
plt.show()

#global sales by dev
average_sales_by_genre = cleaned_gamestats.groupby('Developer')['Global_Sales'].mean()

plt.figure(figsize=(12, 6))
average_sales_by_genre.sort_values().plot(kind='bar', color='green')
plt.ylabel('Average Global Sales')
plt.xlabel('Developer')
plt.title('Global Average Sales by Developer')
plt.xticks(rotation = 360)
plt.show()
#JP sales by genre
average_sales =cleaned_gamestats['JP_Sales'].value_counts()
average_sales_by_genre = cleaned_gamestats.groupby('Genre')['JP_Sales'].mean()

plt.figure(figsize=(12, 6))
average_sales_by_genre.sort_values().plot(kind='bar', color='green')
plt.ylabel('Average Sales')
plt.xlabel('Genre')
plt.title('Average Sales in JP by Genre')
plt.xticks(rotation = 360)
plt.show()

#JP sales by dev
average_sales_by_genre = cleaned_gamestats.groupby('Developer')['JP_Sales'].mean()

plt.figure(figsize=(12, 6))
average_sales_by_genre.sort_values().plot(kind='bar', color='green')
plt.ylabel('Average Sales')
plt.xlabel('Genre')
plt.title('Average Sales in JP by Developer')
plt.xticks(rotation = 360)
plt.show()

#NA sales by genre
average_sales =cleaned_gamestats['NA_Sales'].value_counts()
average_sales_by_genre = cleaned_gamestats.groupby('Genre')['NA_Sales'].mean()

plt.figure(figsize=(12, 6))
average_sales_by_genre.sort_values().plot(kind='bar', color='green')
plt.ylabel('Average Sales')
plt.xlabel('Genre')
plt.title('Average Sales in NA by Genre')
plt.xticks(rotation = 360)
plt.show()

#NA sales by dev
average_sales_by_genre = cleaned_gamestats.groupby('Developer')['NA_Sales'].mean()

plt.figure(figsize=(12, 6))
average_sales_by_genre.sort_values().plot(kind='bar', color='green')
plt.ylabel('Average Sales')
plt.xlabel('Genre')
plt.title('Average Sales in NA by Developer')
plt.xticks(rotation = 360)
plt.show()


#critic score by sales
cleaned_gamestats['Critic_Score_Rounded'] = cleaned_gamestats['Critic_Score'].apply(lambda x: round(x/10))
average_sales_by_genre = cleaned_gamestats.groupby('Critic_Score')['Global_Sales'].mean()

plt.figure(figsize=(12, 6))
plt.scatter(cleaned_gamestats['Critic_Score'], cleaned_gamestats['Global_Sales'], alpha=0.5)
plt.xlabel('Critic Score ')
plt.ylabel('Average Sales')
plt.title('Average Sales vs Critic Score')

coefficients = np.polyfit(cleaned_gamestats['Critic_Score'], cleaned_gamestats['Global_Sales'], 1)
line_of_best_fit = np.poly1d(coefficients)

# Plot the line of best fit
plt.plot(cleaned_gamestats['Critic_Score'], line_of_best_fit(cleaned_gamestats['Critic_Score']),
         color='red', label='Line of Best Fit')
slope = coefficients[0] * 10
print(f"Slope of the line of best fit: {slope}")
plt.show()

#user score by sales    
cleaned_gamestats['User_Score_Rounded'] = cleaned_gamestats['User_Score'].apply(lambda x: round(x))
average_sales_by_genre = cleaned_gamestats.groupby('User_Score_Rounded')['Global_Sales'].mean()


plt.figure(figsize=(12, 6))
plt.scatter(cleaned_gamestats['User_Score'], cleaned_gamestats['Global_Sales'], alpha=0.5)
plt.xlabel('User Score')
plt.ylabel('Average Sales')
plt.title('Average Sales vs User Score')
coefficients = np.polyfit(cleaned_gamestats['User_Score'], cleaned_gamestats['Global_Sales'], 1)
line_of_best_fit = np.poly1d(coefficients)

# Plot the line of best fit
plt.plot(cleaned_gamestats['User_Score'], line_of_best_fit(cleaned_gamestats['User_Score']),
         color='red', label='Line of Best Fit')
slope = coefficients[0]
print(f"Slope of the line of best fit: {slope}")
plt.show()
