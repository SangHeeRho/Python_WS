
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('./data/gapminder.tsv',sep='\t')
number_of_rows=df.shape[0]
print(number_of_rows,"\n\n")

last_row_index=number_of_rows-1

print(df.loc[last_row_index])


# In[2]:


print(df.loc[len(df)-1])


# In[3]:


print(df.tail(n=1))


# In[4]:


print(df.tail(n=2))


# In[5]:


print(df.loc[[0,99,999]])

