
# coding: utf-8

# In[2]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')

multi_group_var=df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)


# In[3]:


print(multi_group_var.mean())
print(multi_group_var.mean().count())

