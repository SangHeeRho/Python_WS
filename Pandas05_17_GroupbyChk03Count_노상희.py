
# coding: utf-8

# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[3]:


print(df.groupby('continent')['year'].count())


# In[4]:


print(df.groupby('continent'))


# In[7]:


df['year'].unique()
uniList1=df['year'].unique()
print(uniList1)
type(uniList1)


# In[9]:


for idx in uniList1:
    print(idx,"====> 1 :")
    grYear = df[df['continent']==idx]
    print(len(grYear),"\n====>2 \n:",grYear.head(3),"\n====>3 :",grYear.shape)

