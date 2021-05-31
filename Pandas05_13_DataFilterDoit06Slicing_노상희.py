
# coding: utf-8

# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[3]:


df.head(3)


# In[4]:


subset=df.iloc[:,:3]
subset.head()


# In[5]:


subset=df.iloc[:,0:6:2]


# In[6]:


subset.head()


# In[7]:


print(df.iloc[[0,99,999],[0,3,5]])


# In[8]:


print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])


# In[9]:


print(df.loc[10:13,['country','lifeExp','gdpPercap']])


# In[10]:


print(df.iloc[10:13,[0,3,-1]])

