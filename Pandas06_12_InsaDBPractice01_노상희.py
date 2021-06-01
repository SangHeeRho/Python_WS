
# coding: utf-8

# In[28]:


import pandas #헤더에 columns 추가하기
dept=pandas.read_csv('./data/deptDB.csv',header=None)
sawon=pandas.read_csv('./data/sawonDB.csv',header=None)
gogek=pandas.read_csv('./data/gogekDB.csv',header=None)


# In[32]:


dept.columns=['deptno','dname','loc']


# In[35]:


sawon.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']


# In[36]:


gogek.columns=['gobun','goname','gotel','gojumin','godam']


# In[37]:


print(dept)


# In[38]:


print(sawon)


# In[39]:


print(gogek)

