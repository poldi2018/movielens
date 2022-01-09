import pyreadr
#result = pyreadr.read_r('./data/dataset.rds')
result = pyreadr.read_r('./data/validation.rds')

df=result[None]
# conversion of dataframe to dictionary
dic = df.to_dict()
# get column names
# keys: userId, movieId, rating, timestamp, title, genres
columns = list(dic.keys())

def get_rows():
    # question 1
    rows = 0
    for row in dic["title"]:
        rows += 1
    return rows

def ratecount(float):
    rating=float
    ratecount = 0
    for value in dic["rating"].values():
        if value == rating:
            ratecount += 1
    return ratecount

def moviecount():
    movie_count = 0
    x = df.duplicated()
    if x.any():
        print('There are duplicates!')
        df.drop_duplicates(inplace = True)
    else:
        print('There are NO duplicates!')
    for movie in dic["movieId"]:
        movie_count += 1
    return movie_count

def get_users():
    usercount = 0
    for user in dic["userId"].values():
        if user > usercount:
            usercount = user
    return usercount

def has_been_rated(str):
    key=str
    if dic['rating'][key] > 0:
        return True
    else:
        return False 

def ratings_genre(dict):
    genres = dict
    counter=0
    for key, value in dic['genres'].items():
        for key2 in genres.keys():
            if key2 in value:
                if has_been_rated(key):
                    genres[key2] = genres[key2]+1
        counter+=1
        # this testcounter was used to keep the dataset shorter
        # if counter == 200:
        #     break
    return genres


def questions():
    # question 1
    rows=get_rows()
    print('The movielens quizz! \r\n \r\n1. How many rows and columns are \
            there in the dataset?')
    print('Answer: There are', rows, 'rows and', len(columns), 'columns in the dataset. \r\n')

    # question 2a
    rated_zeros = ratecount(0.0)
    print('How many zeros were given as ratings in the dataset?')
    print('Answer: ', rated_zeros, 'movies rated with 0 \r\n')

    # question 2b
    rated_threes = ratecount(3.0)
    print('How many threes were given as ratings in the dataset?')
    print('Answer: ', rated_threes, 'movies rated with 3 \r\n')

    # question 3
    movie_count = moviecount()
    print('How many different movies are there in the dataset?')
    print('Answer: There are', movie_count, 'movies in the dataset. \r\n')

    # question 4
    usercount = get_users()
    print('How many different users are there in the dataset?')
    print('Answer: There are', usercount, 'different users in the dataset. \r\n')

    # question 5
    genres = {'Drama': 0, 'Comedy': 0, 'Thriller': 0, 'Romance': 0}
    returned_ratings = ratings_genre(genres)
    print('How many movie ratings are in each of the following genres in the dataset?')
    print('Drama: ', returned_ratings['Drama'], 'ratings |', 'Comedy: ',returned_ratings['Comedy'], 'ratings |')
    print( 'Thriller: ', returned_ratings['Thriller'], 'ratings |', 'Romance: ', returned_ratings['Romance'], 'ratings')


questions()
