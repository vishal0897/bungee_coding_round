#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[9]:


match = pd.read_csv("C:/Users/kanoj/OneDrive/Desktop/internship-test2-master/input/question-3/main.csv")


# In[10]:


match


# In[13]:


color = match[['Team','Yellow Cards','Red Cards']]
color


# In[14]:


color.sort_values(by=['Red Cards','Yellow Cards'],ascending=False)



# In[ ]:




