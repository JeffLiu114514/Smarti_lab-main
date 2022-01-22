import requests, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from bs4 import BeautifulSoup
import json, tqdm

########## GET METADATA ##########

# get all assets
api_key = 'b3252862-709d-48cc-bc8b-60798c5378e5'
reqs = requests.get('https://data.messari.io/api/v2/assets',
                    headers={"x-messari-api-key": api_key})
assets = json.loads(reqs.text)

chain_names = [assets['data'][i]['name'] for i in range(20)]
chain_codes = [assets['data'][i]['symbol'] for i in range(20)]

code = 'LUNA'
metrics = 'mcap.dom'
col_names = ['chain', 'timestamp', 'metric_name', 'value']
row_dict = {col_names[i]: 0 for i in range(len(col_names))}


# %%
from datetime import date
import time
all_metrics = ['act.addr.cnt', 'mcap.dom', 'staking.total.pct', 'twitter.followers']
# all_metrics = ['mcap.dom', 'staking.total.pct', 'twitter.followers']
# all_metrics = ['act.addr.cnt']

final_df = []
for metrics in all_metrics:
	print(metrics)
	for code in tqdm.tqdm(chain_codes):
		url = 'https://data.messari.io/api/v1/assets/{cname}/metrics/{metrics}/time-series'.format(
			cname=code, metrics=metrics)
		reqs = requests.get(url, headers={"x-messari-api-key": api_key})
		dct = json.loads(reqs.text)
		if 'error_code' in dct['status'].keys():
			print(code, 'gg')
			continue
		elif dct['data']['values'] is None:
			print(code, 'gg')
			continue
		else:
			for r in dct['data']['values']:
				new_dict = row_dict.copy()
				new_dict['chain'] = code
				new_dict['metric_name'] = metrics
				new_dict['timestamp'] = r[0]
				new_dict['value'] = r[1]
				final_df.append(new_dict)
		time.sleep(2)

# %% EXPORT
from datetime import datetime
d = pd.DataFrame(final_df)
d['timestamp'] = d.timestamp.apply(lambda a: a/1000).apply(datetime.fromtimestamp)

today = date.today()
d.to_csv('onchain_data_tracking/Data/Messari/' + \
        '{}.{}-'.format(today.month, today.day) + \
        '{}.csv'.format('|'.join(all_metrics)))





