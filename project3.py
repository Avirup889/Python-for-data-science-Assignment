#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


import numpy as np


# In[9]:


df=pd.DataFrame(np.random.randn(4,5),index=['Row1','Row2','Row3','Row4'],columns=["Column1","Column2","Column3","Column4","Column5"])


# In[10]:


df.head()


# In[11]:


df.describe()


# In[ ]:




