import pyreadr
import json
#result = pyreadr.read_r('./data/dataset.rds')
result = pyreadr.read_r('./data/validation.rds')

df=result[None]
# conversion of dataframe to dictionary
dic = df.to_dict()

# get the column names
# keys: userId, movieId, rating, timestamp, title, genres
object_list = pyreadr.list_objects('./data/validation.rds')
columns = object_list[0]['columns']

def questions():
    # question 1
    # rowcount is decreased by 1 for the indices
    rows = 0
    for row in dic["title"]:
        rows = rows+1

    print('1. How many rows and columns are there in the dataset?')
    print('Answer: There are', rows-1, 'rows and', len(dic.keys()), 'columns in the dataset. \r\n')

    # question 2a
    rating_zeros=0
    for value in dic["rating"].values():
        if value==0.0:
            rating_zeros+=1

    print('How many zeros were given as ratings in the dataset?')
    print('Answer: ', rating_zeros, 'movies rated with 0 \r\n')

    # question 2b
    rating_threes=0
    for value in dic["rating"].values():
        if value==3.0:
            rating_threes+=1
    print('How many threes were given as ratings in the dataset?')
    print('Answer: ', rating_threes, 'movies rated with 3 \r\n')


    # question 3
    movies = 0
    for movie in dic["movieId"]:
        movies+=1
    print('How many different movies are there in the dataset?')
    print('Answer: There are', movies-1, 'movies in the dataset. \r\n')




questions()

