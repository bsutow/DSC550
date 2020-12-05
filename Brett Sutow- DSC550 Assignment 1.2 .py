#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 


# In[3]:


#Practice attempt#
np.random.rand(4,2)


# In[4]:


#Practice attempt creating 4 by 3#
np.random.randint(0,501, size = (4,3))


# In[46]:


#Creates randomly generate array sized 10x50 with 1 to 500#
x= np.random.randint(1,501, size = (10,50))
print(x)


# In[47]:


#Provides sum of columns#
x.sum(axis=0)


# In[48]:


#Provides sum of rows#

x.sum(axis=1)


# In[49]:


#Provides sum#
x.sum()


# In[50]:


#Provides min#
x.min()


# In[51]:


#Provides max#
x.max()


# In[52]:


#Provides mean#
x.mean()


# In[53]:


#Provides standard deviation#
x.std()


# In[54]:


#Sorts overall by columns#
np.sort(x, axis=0)


# In[55]:


#Sorts overall by rows#
np.sort(x, axis=1)


# In[56]:


#Sorts columns by 2#
sortedcol = x[x[:,1].argsort()]
sortedcol


# In[57]:


#Sorts rows by 2#
sortedrow = x[:, x[1].argsort()]
sortedrow


# In[ ]:





# In[ ]:




