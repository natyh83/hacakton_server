import csv

users_rating_db_path = '../../db/user_ratings.csv'


class Users_model:
    def __init__(self):
        users_ratings = {}
        with open(users_rating_db_path, 'r') as f:
            reader = csv.reader(f)
            is_first = True
            for row in reader:
                if is_first == True:
                    is_first = False
                    continue

                user_id = row[1]
                users_ratings[user_id] = {
                    'terms': row[2],
                    'loyality': row[3],
                    'engagement': row[4],
                    'fulfillment': row[5],
                    'motivation': row[6]
                }

        self.users_ratings_db = users_ratings

    def get_user_ratings_by_id(self, user_id):
        print('user model, ratings: ' + user_id)
        return self.users_ratings_db[user_id]
