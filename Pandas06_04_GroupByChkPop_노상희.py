
# coding: utf-8

# In[2]:


#날짜 unique 값 << pop
import pandas as pd
df=pd.read_csv('./data/gapminder.tsv',sep='\t')


# In[10]:


print(df.groupby('year')['pop'].count()) #연도 기준 인구수 카운트


# In[12]:


df['pop'].unique()
uniqueList=df['pop'].unique()
print(uniqueList)
type(uniqueList)


# In[13]:


for idx in uniqueList:
    print(idx, "=====> 1 : ")
    yearList=df[df['year']==idx]
    print(len(yearList),"\n====>2 \n",yearList.head(3),yearList.shape)
    print(yearList['pop'].mean())

