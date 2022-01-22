import twitterbot as tb
import secrets, sys
hashtag = 'bitcoin'# sys.argv[1]
credentials = secrets.get_credentials()
bot = tb.Twitterbot(credentials['email'], credentials['password'])
# logging in
bot.login()
# calling like_retweet function
bot.like_retweet(hashtag)