from tweepy_tools import *
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

twts = api.user_timeline(user_id=1419920719698219008, count=5000)

a = twts[0]

tweets_entry = ['created_at', 'favorite_count', 'id', 'text']

def plot_3_graphs(df, title_append='all'):
	df.favorite_count.hist()
	plt.title(title_append+' Distribution of number favorite in the ' + str(df.shape[0]) + ' Tweets');
	plt.show()
	df.created_at.hist()
	plt.xticks(rotation=15);
	plt.title(title_append+' Time Distribution of Tweets');
	plt.show()
	df.retweet_count.hist();
	plt.title(title_append+' Number of Retweet distribution');
	plt.show()


df = pd.DataFrame([{'created_at': t.created_at,
                    'favorite_count': t.favorite_count,
                    'retweet_count': t.retweet_count,
                    'id': t.id,
                    'text': t.text} for t in twts])
plot_3_graphs(df)

# most recent week
df['created_at'] = df.created_at.apply(pd.to_datetime).dt.date
df1 = df[df.created_at > pd.to_datetime(datetime.now() - timedelta(weeks=1))]


plot_3_graphs(df1, title_append='last week: ')




