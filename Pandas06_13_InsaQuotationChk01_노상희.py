
# coding: utf-8

# In[10]:


import pandas #헤더에 columns 추가하기
dept=pandas.read_csv('./data/deptDB.csv',header=None)
sawon=pandas.read_csv('./data/sawonDB.csv',header=None)
gogek=pandas.read_csv('./data/gogekDB.csv',header=None)


# In[11]:


dept.columns=['deptno','dname','loc']


# In[12]:


sawon.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']


# In[13]:


gogek.columns=['gobun','goname','gotel','gojumin','godam']


# In[14]:


print(dept)


# In[15]:


print(sawon)


# In[16]:


print(gogek)


# In[18]:


gogek=gogek.replace("'", " ", regex=True)
print(gogek)


# In[19]:


dept=dept.replace("'", " ", regex=True)
print(dept)


# In[20]:


sawon=sawon.replace("'", " ", regex=True)
print(sawon)

