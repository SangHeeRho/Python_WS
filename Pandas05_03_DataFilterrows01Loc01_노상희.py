
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
df


# In[4]:


df.loc['viper']


# In[6]:


df.iloc[0]


# In[7]:


df.loc[0]


# In[8]:


df.loc['cobra':'viper', 'max_speed']


# In[9]:


df.loc[[False,False,True]]


# In[10]:


df.loc[df['shield']>6]


# In[11]:


df.loc[df['shield']>6,['max_speed']]

