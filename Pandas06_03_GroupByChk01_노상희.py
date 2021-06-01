
# coding: utf-8

# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[6]:


type(df)


# In[4]:


type(df['pop'])


# In[7]:


grouped_year_df=df.groupby('year') #year
print(type(grouped_year_df))
print(grouped_year_df["pop"])


# In[8]:


grouped_year_df["pop"].mean()

