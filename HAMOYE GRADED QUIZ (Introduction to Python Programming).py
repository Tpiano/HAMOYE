#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('C:/Users/USER/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding = 'latin-1')


# In[68]:


df.head()


# In[7]:


df.shape


# In[25]:


country = df['Area'].unique()
num_country = len(set(country))
num_country


# In[85]:


df['Y2017'].describe() #2dp


# In[42]:


Y2017_min = df.groupby('Area')['Y2017'].min()
Y2017_max = df.groupby('Area')['Y2017'].max()


# In[44]:


Y2017_min


# In[40]:


Y2017_max


# In[73]:


Processing_sum = df.groupby('Element')['Y2017'].sum()
Processing_sum


# In[55]:


highest_sum = df.groupby('Element')[].sum()
highest_sum.sum()


# In[65]:


# df['Y2014'].corr()


# In[71]:


df.isna().sum()


# In[81]:


protein_supply = df.groupby('Element',)['Y2015'].sum()
protein_supply


# In[ ]:




