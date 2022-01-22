import tweepy
import tqdm
import pandas as pd
import matplotlib.pyplot as plt


consumer_key = 'KfHjRyhYXAqz9lGotoEvMZFwQ'
consumer_secret = 'NtrCMEfkINA5oNM01CrMG0aS0FjlXJT24fBrKQb4YWju5sIgYT'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANSMXgEAAAAAYsISPsWSO1QHZNyAs3VpKH36UuA%3DMQCQFNhPeoA8JUan60NIsoCA5NR49UkR9d1MOMe3NYepQPveFI'
access_token = '1053059048281649152-WDy59JcSWjSCsBNithCf3Od4xsagai'
access_token_secret = 'esDNNpHGuREihBlqWFmGWwiSntgKFA9cYAW8ggI8pD8EX'
# OAuth 2.0 stuff 
Client_ID = 'cS03bGVhVVEtLW9WXzI2ZENPSmo6MTpjaQ'
Client_Secret = 'Zfgjq640_TyFU18YM-z2avRDUTApj42GYt-fM3TllxisoV1NOQ'



# jessy stuff 
# Consumer Keys ---
# API Key
consumer_key = 'N4YdPodeTYW1cozqggYHOSsKD'
# API Key Secret
consumer_secret = 'H8lwk3oWzQsrmG6lVgvpVSic2D23PLeXtNFGnu95XL6NBov6jL'
# Authentication Tokens ---
# Bearer Token
bearer_token = 'AAAAAAAAAAAAAAAAAAAAALRJSwEAAAAAzLz7p3AIyKMOJUoCHYu3itj6ezQ%3DA3uB0kY0Fq0TgPDeEmgdti2E4ZdkWt3XGld85YzSw7IjEjwYfd'
access_token = '1361623863629516808-JFp9sX7U2ZGK177lA1OUZ9W0rstIBB'
access_token_secret = 'o78sjDdePKBGFVbVWUZ8JP9BzWNsZ3a2pW3pyd0ZXZqfn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



# API v1.1 
# u = api.get_user(user_id='1361623863629516808') # OR: (screen_name='0xy42')
# u = api.get_user(screen_name='@balajis')
# u.created_at # 2. get user onboarding time
# u.description # 1. get user description
# u.followers_count  #  get user number of follower "
# u.name # display name
# # get following ids
# friend_ids = api.get_friend_ids(user_id='1361623863629516808')


# # API v2.0
# client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,access_token=access_token, access_token_secret=access_token_secret)
# l = client.get_users_followers(id='1053059048281649152')
# u = client.get_user(username='cz_binance')
# u = client.get_user(id='733478230779428865')
# u.username
# client.get_users_tweets(id='733478230779428865')





################ TEST THE WORKFLOW ##################

# balajis
def get_single_user(user_id):
	u = api.get_user(user_id=user_id)
	return {'name': u.name,
           'created_at': u.created_at,
           'description': u.description,
           'followers_count': u.followers_count,
           'id': u.id,
           'screen_name': u.screen_name,
           'favourites_count': u.favourites_count,
           'entities': u.entities,
           'friends_count': u.friends_count,
           'location': u.location,
           'url': u.url,
           'verified': u.verified}

def get_friend_info(screen_name='balajis'):
	following_ids = api.get_friend_ids(screen_name=screen_name)
	following_users = []
	for id in tqdm.tqdm(following_ids):
		following_users.append(api.get_user(user_id=id))
	flwing_df = pd.DataFrame([{'name': u.name,
	                           'created_at': u.created_at,
	                           'description': u.description,
	                           'followers_count': u.followers_count,
	                           'id': u.id,
	                           'screen_name': u.screen_name,
	                           'favourites_count': u.favourites_count,
	                           'entities': u.entities,
	                           'friends_count': u.friends_count,
	                           'location': u.location,
	                           'url': u.url,
	                           'verified': u.verified}
	                          for u in following_users])
	flwing_df.drop_duplicates(inplace=True)
	flwing_df.to_csv('/Users/qitianhu/Desktop/Smarti_lab/export/'+screen_name+'-friends-all.csv')
	return flwing_df

