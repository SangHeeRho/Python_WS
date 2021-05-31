
# coding: utf-8

# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[3]:


print(df.groupby('continent')['year'].nunique(),"\n===>")
print(df.groupby('continent')['year'].unique(),"\n====>")
print(df.groupby('continent')['year'].unique()['Africa'],"\n====>")

