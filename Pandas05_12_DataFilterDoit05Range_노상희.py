
# coding: utf-8

# In[1]:


import pandas


# In[3]:


df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[4]:


small_range=list(range(5))
print(small_range)


# In[5]:


print(type(small_range))


# In[6]:


df.head(3)


# In[7]:


subset=df.iloc[:,small_range]
print(subset.head())


# In[8]:


small_range=list(range(3,6))
print(small_range)


# In[10]:


subset=df.iloc[:,small_range]
subset


# In[11]:


small_range=list(range(0,6,2))
subset=df.iloc[:,small_range]
print(subset.head())

