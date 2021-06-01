
# coding: utf-8

# In[7]:


import pandas as pd
df=pd.read_csv('./data/gapminder.tsv',sep='\t')
print(df.groupby('continent')['lifeExp'].count())


# In[8]:


grouped_con_df=df.groupby('continent')
print(type(grouped_con_df))
print(grouped_con_df['lifeExp'])


# In[10]:


grouped_con_df['lifeExp'].mean()

# for idx in uniList:
#     print(idx)
#     grYear=df[df['year']==idx]
#     print(len(grYear),"\n====>2 \n",grYear.head(3),grYear.shape)
#     print(grYear['lifeExp'].mean())

