import json, pandas as pd, matplotlib.pyplot as plt, tqdm
import seaborn as sns

# %% POKTscan data
d = pd.read_csv('onchain_data_tracking/Data/POKTscan/final_df-1.18.csv')
d['first_time'] = d['first_time'].apply(pd.to_datetime)
d['first_time'] = d['first_time'].apply(lambda a: a.tz_localize(None))

sns.lineplot(data=d, x='first_time', y='total_relays', hue='chain');plt.show()

d.plot('first_time', 'total_relays'); plt.show()












