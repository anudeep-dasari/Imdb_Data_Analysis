# Import Libraries
import pandas as pd
import numpy as np

# Import the data
df = pd.read_csv('imdb_top_1500.csv', encoding="ISO-8859-1")

# Cleaning Columns
# Splitting the Directors and Actors column int two dfiferent columns
df['Directors and Actors'] = df['Directors and Actors'].str.split('|')
df['Director'] = df['Directors and Actors'].str[0]
df['Actor'] = df['Directors and Actors'].str[1]

df['Director'] = df['Director'].str.split('-')
df['Director1'] = df['Director'].str[2]
df['Director2'] = df['Director'].str[3]

df['Actor'] = df['Actor'].str.split('-')
df['Actor1'] = df['Actor'].str[2]
df['Actor2'] = df['Actor'].str[3]
df['Actor3'] = df['Actor'].str[4]
df['Actor4'] = df['Actor'].str[5]

# remove the unwanted columns
df = df.drop(['Directors and Actors','Director','Actor'],axis=1)


# Splitting the Genres
df['Genres'] = df['Genre'].str.split(' ')
df['Genre1'] = df['Genres'].str[0]
df['Genre2'] = df['Genres'].str[1]
df['Genre3'] = df['Genres'].str[2]

#df['is_animated'] = df['Genre'].str.contains('Animation')
#df['is_Adventure'] = df['Genre'].str.contains('Adventure')
#df['is_Crime'] = df['Genre'].str.contains('Crime')
#df['is_Comedy'] = df['Genre'].str.contains('Comedy')
#df['is_Drama'] = df['Genre'].str.contains('Drama')
#df['is_Sci-Fi'] = df['Genre'].str.contains('Sci-Fi')
#df['is_Thriller'] = df['Genre'].str.contains('Thriller')
#df['is_Horror'] = df['Genre'].str.contains('Horror')
#df['is_Fantasy'] = df['Genre'].str.contains('Fantasy')
#df['is_Biography'] = df['Genre'].str.contains('Biography')
#df['is_Mystery'] = df['Genre'].str.contains('Mystery')
#df['is_Romance'] = df['Genre'].str.contains('Romance')
#df['is_Sport'] = df['Genre'].str.contains('Sport')
#df['is_War'] = df['Genre'].str.contains('War')
#df['is_Western'] = df['Genre'].str.contains('Western')

df = df.drop(['Genres'],axis=1)

# Cleaning the Runtime 
df['Runtime'] = df['Runtime'].str.replace(' min','').astype(int)


# Cleaning the Gross
df['Gross'] = df['Gross'].str.replace('$','') 
df['Gross'] = df['Gross'].str.replace('M','')
df['Gross'] = df['Gross'].astype(float)

# Cleaning Release date
df['Release'] =  df['Release'].str.replace('I','')
df['Release'] =  df['Release'].str.replace('II','')
df['Release'] =  df['Release'].str.replace('III','')
df['Release'] =  df['Release'].str.replace('IX','')
df['Release'] =  df['Release'].str.replace('X','')
df['Release'] =  df['Release'].astype(int)
df['Years since Release'] = df['Release'].apply(lambda x: 2021-x)


# write the modified data to new csv
df.to_csv('cleaned_imdb_data.csv',encoding='ISO-8859-1', index=False)












