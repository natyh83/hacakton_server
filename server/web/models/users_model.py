import csv

users_rating_db_path = '../../db/user_ratings.csv'
users_engagement_db_path = '../../db/user_engagement.csv'


class Users_model:
    def __init__(self):
        users_ratings = {}
        users_engagement = {}
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

        with open(users_engagement_db_path, 'r') as f:
            reader = csv.reader(f)
            is_first = True
            for row in reader:
                if is_first == True:
                    is_first = False
                    continue

                user_id = row[1]
                date = row[2]
                engagement = row[3]

                if user_id not in users_engagement:
                    users_engagement[user_id] = {}

                users_engagement[user_id][date] = engagement
        self.users_engagement_db = users_engagement



    def get_user_ratings_by_id(self, user_id):
        print('user model, ratings: ' + user_id)
        return self.users_ratings_db[user_id]

    def get_user_engagement_by_id(self, user_id):
        print('user model, engagement: ' + user_id)
        return self.users_engagement_db[user_id]