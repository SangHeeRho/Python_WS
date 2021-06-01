
# coding: utf-8

# In[3]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[4]:


global_yearly_life_expectancy=df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)


# In[5]:


global_yearly_life_expectancy.plot()

