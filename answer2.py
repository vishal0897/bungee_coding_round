#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


user = pd.read_csv("C:/Users/kanoj/OneDrive/Desktop/internship-test2-master/input/question-2/main.csv")


# In[7]:


user


# In[8]:


user.groupby('occupation')['age'].agg(['min','max'])


# In[ ]:




