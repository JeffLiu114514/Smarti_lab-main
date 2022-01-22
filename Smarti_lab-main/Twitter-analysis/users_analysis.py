KOL_list = ['ajm_alameda', 'realsatoshinet', 'Vince_Van_Dough', 'dhof', 'mrjasonchoi', 'mrjasonchoi', 'LeePima', 'SinoGlobalCap',
'zepump', '0xminion', 'reganbozman', 'zhusu', '0xMaki', '0xttk', 'Shuyao_Kong', 'Luyaoyuan1', 'DegenPing', 'sid_coelho', 'defiyield_app', 'vfat0']

c = 0
following_ids = []
for kol in tqdm.tqdm(KOL_list):
	following_ids += api.get_friend_ids(screen_name=kol)
print('fin!')



a1 = api.get_followers(user_id=2178012643, cursor=-3).next_cursor()
a2 = api.get_followers(user_id=2178012643)
a3 = api.get_followers(user_id=2178012643)
a4 = api.get_followers(user_id=2178012643)


ids = pd.DataFrame(following_ids)
ids = pd.DataFrame(ids[0].value_counts())
ids['kol_count'] =ids[0]# .rename({0:'id'})
ids['id'] = ids.index
del ids[0]

# add
df = pd.read_csv('export/KOL1-following-unique.csv')
df['kol_count'] = 0
df3 = pd.merge(df, ids, how='left', on='id')
df = df3




a = []
for f in following_ids:
	a += f
kol_cnt = pd.DataFrame(pd.DataFrame(a, columns=['id']).value_counts())

following_ids_unique = list(set(a))
done_idx, total_user_info = [], []
for i in tqdm.tqdm(range(len(following_ids_unique))):
	if i not in done_idx:
		total_user_info.append(get_single_user(following_ids_unique[i]))
		done_idx.append(i)
len(total_user_info)
df = pd.DataFrame(total_user_info)
df.to_csv('export/KOL1-following-unique-kol.csv')

keywords = ['protocol', 'finance', 'DAO', 'HQ', 'app', 'xyz', 'lab']
df1 = df[(df.created_at.apply(pd.to_datetime) > pd.Timestamp('2021-06-01 00:00:00+0000', tz='UTC'))
		& (df.followers_count < 10000)
         & (df.followers_count > 800)
         & df.description.str.contains('|'.join(keywords))]
df1 = df1.sort_values(by='kol_count', ascending=False)
df.description.str.contains('|'.join(keywords))
df1.to_csv('export/KOL1-following-unique-kol-filtered.csv')
# df1 = pd.read_csv('/Users/qitianhu/Desktop/KOL1-following-unique-filtered.csv')
