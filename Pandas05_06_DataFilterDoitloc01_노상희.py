
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


df=pd.read_csv('./data/gapminder.tsv',sep='\t')


# In[19]:


df.head(3)


# In[20]:


df.shape


# In[21]:


loc00=df.loc[0]


# In[22]:


print(loc00) ; type(loc00)


# In[23]:


df.loc[90:100]


# In[24]:


print(df.loc[99])


# In[25]:


df.tail(3)


# In[26]:


#-1과 같이 인덱스에 없는 값을 사용하면 오류가 발생
print(df.loc[-1])


# In[27]:


len(df)

