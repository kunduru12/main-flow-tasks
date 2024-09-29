#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
df=pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\anu\\task2.xlsx")
print(df)


# # filtering data based on conditions

# In[14]:


df[df.UCZAA>1.451]


# In[28]:


df.iloc[3:5,:]


# # handling missing values

# In[34]:


df.dropna()


# In[44]:


import pandas as pd
import numpy as np
df=pd.read_excel("C:\\Users\\ANUSHA\\Desktop\\anu\\task2.xlsx")
print(df)
df.dropna(inplace=True)


# In[45]:


df.fillna("missing")


# # calculating summary statistics

# In[46]:


df.describe()


# In[ ]:




