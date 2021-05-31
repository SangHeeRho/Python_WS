import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')
country_df=df['country']
print(type(country_df))
print(country_df.head()) 
print(country_df.tail())
subset=df[['country','continent','year']]
print(type(subset))
print(subset.head())
print(subset.tail())

#한 줄만 입력할때는 print 불필요
subset=df[['country','continent','year']]
subset.head(1)