
# coding: utf-8

# In[29]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[30]:


uniqueyear=df['year'].unique()
uniquecon=df['continent'].unique()


# In[37]:


for i in uniqueyear:
    yearlist=df[df['year']==i]
    for j in uniquecon:
        conlist=yearlist[df['continent']==j]
        print(f"{i}년 {j:^10}지역 기대수명 평균 : {conlist['lifeExp'].mean():.2f}   gdp 평균 : {conlist['gdpPercap'].mean():.2f}")

