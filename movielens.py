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
    print('Answer: There are', rows-1, 'rows and', len(dic.keys()), 'columns in the dataset.')

   

questions()

