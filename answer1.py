#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[37]:


c=pd.read_csv("C:/Users/kanoj/OneDrive/Desktop/internship-test2-master/input/question-1/main.csv")


# In[38]:


c


# In[39]:


c.Year = pd.to_datetime(c.Year,format='%Y')
c.Year


# In[40]:


c = c.set_index('Year',drop=True)
c


# In[41]:


del c['Total']
c.head()


# In[44]:


cp = c.resample('10AS').sum()

p = cp['Population'].resample('10AS').max()
print(p)
cp['Population'] = p
cp


# In[ ]:




