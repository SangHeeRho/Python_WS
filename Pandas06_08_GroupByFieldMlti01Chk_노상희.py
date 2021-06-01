
# coding: utf-8

# In[1]:


import pandas
df=pandas.read_csv('./data/gapminder.tsv',sep='\t')


# In[2]:


uniqueyear=df['year'].unique()
uniquecon=df['continent'].unique()


# In[3]:


for i in uniqueyear:
    yearlist=df[df['year']==i]
    for j in uniquecon:
        conlist=yearlist[df['continent']==j]
        print(f"{i}년 {j:^10}지역 기대수명 평균 : {conlist['lifeExp'].mean():.2f}   gdp 평균 : {conlist['gdpPercap'].mean():.2f}")


# In[4]:


print(df.head(3), "\n------")
multi_group_var=df.groupby(['year','continent'])['lifeExp','gdpPercap'].mean()
print(multi_group_var)

