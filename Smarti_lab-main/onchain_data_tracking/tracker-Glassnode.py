import requests, pandas as pd
import json

from glassnode import GlassnodeClient
gn = GlassnodeClient(api_key='826d60dd-35e1-4957-a850-0cf6ae0ec16c')


# chains = ['BTC', 'ETH', 'AVAX', 'SOL']
# url = 'https://api.glassnode.com/v1/metrics/addresses/{metric}?a={chain_code}'.format(
# 	metric='active_count', chain_code='BTC')
# reqs = requests.get(url)
# dct = json.loads(reqs.text)

final_df = []
for chain_code in ['BTC', 'ETH', 'USDT']:
	d = gn.get(domain='addresses', metric='active_count', params={'a': chain_code})
	for i in range(len(d)):
		d[i]['chain'] = chain_code
	final_df += d.copy()

final_df2 = pd.DataFrame(final_df)

import seaborn as sns
import matplotlib.pyplot as plt
final_df3 = final_df2.sample(100)

sns.lineplot(data=final_df3, x='t', y='v', hue='chain');plt.show()




# Terra
# ethereum
# binance smart chain
# solana
# polkadot
# Aurora (near)
# Near
# Avalanche
# Polygon
# Optimism
# Arbitrum
# Starkware
# ZKSync
# Chainlink
# Cosmos
# Hedera
# Fantom
# Mina
# Aleo Network
# Flow
# Harmony One
# Immutable X
# DYDX

