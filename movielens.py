import pyreadr

# result = pyreadr.read_r('./data/dataset.rds')
result = pyreadr.read_r('./data/validation.rds')
df=result[None]
dic = df.to_dict()
# get column names
# keys: userId, movieId, rating, timestamp, title, genres
columns = list(dic.keys())

def get_rows():
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
    for key, value in dic['genres'].items():
        for key2 in genres.keys():
            if key2 in value:
                if has_been_rated(key):
                    genres[key2] = genres[key2]+1
    return genres

def most_ratings(dict):
    movies_to_check=dict
    winner = {'winner': {'title': '', 'ratings': 0}}
    for movie in movies_to_check:
        for key, value in dic['title'].items():
            if movie in value:
                if dic['rating'][key] != 0.0:
                    movies_to_check[movie] +=1 
    for key, value in movies_to_check.items():
        if value > winner['winner']['ratings']:
            winner['winner']['title'] = key
            winner['winner']['ratings'] = value
    movies_to_check.update(winner)
    return movies_to_check

def common_ratings():
    halfstar = 0
    fullstar = 0
    result = ''
    for rating in dic['rating'].values():
        if rating % 1 == 0.5:
            halfstar+=1
        elif rating % 1 == 0.0:
            fullstar+=1
    if halfstar > fullstar:
        result='halfstars are more common: '+ str(halfstar)+' halfstars vs '+str(fullstar)+' fullstars. So it is false.' 
    else:
        result='fullstars are more common: '+ str(fullstar)+' fullstars vs '+str(halfstar)+' halfstars. So it is true.'
    return result 


def questions():
    # question 1
    rows=get_rows()
    print('\r\n             *** The movielens quizz! *** \r\n \r\nQuestion 1: How many rows and columns are there in the dataset?')
    print('Answer: There are', rows, 'rows and', len(columns), 'columns in the dataset. \r\n')

    # question 2a
    rated_zeros = ratecount(0.0)
    print('Question 2a: How many zeros were given as ratings in the dataset?')
    print('Answer: ', rated_zeros, 'movies rated with 0 \r\n')

    # question 2b
    rated_threes = ratecount(3.0)
    print('Question 2b: How many threes were given as ratings in the dataset?')
    print('Answer: ', rated_threes, 'movies rated with 3 \r\n')

    # question 3
    movie_count = moviecount()
    print('Question 3: How many different movies are there in the dataset?')
    print('Answer: There are', movie_count, 'movies in the dataset. \r\n')

    # question 4
    usercount = get_users()
    print('Question 4: How many different users are there in the dataset?')
    print('Answer: There are', usercount, 'different users in the dataset. \r\n')

    # question 5
    genres = {'Drama': 0, 'Comedy': 0, 'Thriller': 0, 'Romance': 0}
    returned_ratings = ratings_genre(genres)
    print('Question 5: How many movie ratings are in each of the following genres in the dataset?')
    print('Drama: ', returned_ratings['Drama'], 'ratings |', 'Comedy: ',returned_ratings['Comedy'], 'ratings |')
    print( 'Thriller: ', returned_ratings['Thriller'], 'ratings |', 'Romance: ', returned_ratings['Romance'], 'ratings |')

    # question 6
    movies_to_check = {'Forrest Gump': 0, 'Jurassic Park (1993)': 0,
                       'Pulp Fiction': 0, 'Shawshank Redemption': 0,
                       'Speed 2: Cruise Control': 0}
    checked_movies = most_ratings(movies_to_check)
    print('Question 6: Which movie has the greatest number of ratings? \r\n')
    print('Forrest Gump: ', checked_movies['Forrest Gump'], 'ratings |',
          'Jurassic Park (1993) ',checked_movies['Jurassic Park (1993)'],
          'ratings |')
    print('Pulp Fiction: ', checked_movies['Pulp Fiction'], 'ratings |',
          'The Shawshank Redemption: ', checked_movies['Shawshank Redemption'], 'ratings |')
    print('Speed 2: Cruise Control: ', checked_movies['Speed 2: Cruise Control'], 'ratings | \r\n')

    print('THE WINNER IS:', checked_movies['winner']['title'], 'with', checked_movies['winner']['ratings'], 'ratings \r\n')

    # question 8
    print('Question 8: True or False: In general, half star ratings are less common than whole star ratings.')
    print('Answer:', common_ratings(), '\r\n')

questions()
