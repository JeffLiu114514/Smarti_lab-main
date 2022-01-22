################### EXTRACT HISTORICAL RELAY DATA ############################


import json, pandas as pd, matplotlib.pyplot as plt, tqdm
# Note on how to get this data:
# Use the "Network" panel in "Inspect", refresh the table, will see a graphql query
# click into it and copy the data object
# Note on data format: select all the chains with Day as unit
with open('onchain_data_tracking/Data/POKTscan/POKTscan-RelayByDay-1.18.json') as json_file:
	data = json.load(json_file)

d = data['data']['getRelays']['units']
d0 = d[0]
col_names = ['chain', 'total_relays', 'total_pokt', 'point', 'first_time', 'last_time']
row_dict = {col_names[i]: 0 for i in range(len(col_names))}
final_df = []
chainname_conversion = {'0040': 'Harmony Shard 0',
	'0021': 'Ethereum',
	'0005': 'FUSE Mainnet',
	'0009': 'Polygon Mainnet',
	'0028': 'ETH Archival Trace',
	'0027': 'xDAI',
	'0026': 'Ethereum Goerli',
	'0006': 'Solana Mainnet',
	'000C': 'xDAI Archival',
	'0025': 'Ethereum Rinkeby',
	'0004': 'BSC Mainnet',
	'0003': 'Avalanche Mainnet',
	'0001': 'POKT Mainnet',
	'000B': 'Polygon Archival',
	'000A': 'FUSE Archival',
	'0044': 'IoTeX Mainnet',
	'0023': 'Ethereum Ropsten',
	'0024': 'Ethereum Kovan',
	'0022': 'Ethereum Archival'}
for d0 in tqdm.tqdm(d):
	new_dict = row_dict.copy()
	new_dict['point'] = d0['point']
	new_dict['first_time'] = d0['first_time']
	new_dict['first_time'] = d0['first_time']
	for chain in d0['chains']:
		new_dict2 = new_dict.copy()
		for key in ['total_relays', 'total_pokt']:
			new_dict2[key] = chain[key]
		new_dict2['chain'] = chainname_conversion[chain['chain']]
		final_df.append(new_dict2)




################### SCARPE TODAY DATA ############################
from selenium import webdriver
url = 'https://poktscan.com/public/dashboard'
driver = webdriver.Firefox(executable_path='/Users/qitianhu/Documents/Activity/Past/21.6-字节-政经研究战略/民营经济/xjp讲话/geckodriver')
driver.get(url)
chains = driver.find_elements_by_css_selector(".css-1nju2dy").copy()

from datetime import datetime
now = datetime.now()
time_str = now.__str__()

for chain in chains:
	new_dict = row_dict.copy()
	new_dict['chain'] = chain.text.split('\n')[0].split(' (')[0]
	new_dict['total_relays'] = int(chain.text.split('\n')[1].replace(',',''))
	new_dict['first_time'] = time_str
	final_df.append(new_dict)


driver.close()
final_df = pd.DataFrame(final_df)
final_df.to_csv('onchain_data_tracking/Data/POKTscan/final_df-1.18.csv')

