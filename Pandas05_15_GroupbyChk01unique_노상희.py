
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[3]:


print(df.head(n=10))


# In[4]:


print(df.head())


# In[5]:


print(df.groupby('year')['lifeExp'].mean())


# In[6]:


df['year'].unique()


# In[7]:


uniList=df['year'].unique()
print(type(uniList))
print(uniList,"\n====>")

