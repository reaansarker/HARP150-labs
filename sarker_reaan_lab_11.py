#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
with open('AAPL.csv') as aapl:
    aapl_data = csv.reader(aapl)
    my_aapl = [row for row in aapl_data]
my_aapl


# In[3]:


import csv
with open('AAPL.csv') as aapl:
    aapl_data = csv.reader(aapl)
    my_aapl = [row for row in aapl_data]
print(my_aapl)


# In[4]:


import pandas as pd
aapl_stock = pd.read_csv('AAPL.csv')
aapl_stock


# In[5]:


aapl_stock = pd.read_csv('AAPL.csv')
print(aapl_stock)


# In[6]:


aapl_stock.High.loc[0]


# In[7]:


aapl_stock[['Date', 'High']]


# In[8]:


aapl_stock.describe()


# In[9]:


aapl_stock.head(4)


# In[10]:


aapl_stock.tail(4)


# In[11]:


aapl_stock.sample(4)


# In[13]:


aapl_stock.shape


# In[14]:


aapl_stock.dtypes


# In[15]:


aapl_stock.columns


# In[20]:


aapl_stock.duplicated()


# In[21]:


from matplotlib import pyplot as plt

import numpy as np


# In[22]:


aapl_g1 = np.linspace(-10, 10, 500)
plt.plot(aapl_g1, np.sin(aapl_g1))


# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
aapl_g2 = aapl_stock.drop ('Volume', axis = 1)
aapl_g2.plot()


# In[25]:


from matplotlib import pyplot as plt

import numpy as np


# In[26]:


aapl_stock['High'].value_counts().head().plot(kind='bar')


# In[1]:


#post lab ex


# In[2]:


import csv
with open('job_skills.csv') as job:
    job_data = csv.reader(job)
    my_job = [row for row in job_data]
my_job


# In[3]:


import pandas as pd
job_skills = pd.read_csv('job_skills.csv')
job_skills


# In[4]:


job_skills.head(4)


# In[5]:


job_skills.tail(4)


# In[6]:


job_skills.sample(4)


# Pandas is useful to use for data manipulation, visualization, and analysis. 
# for col in df.columns:
#     series = df[col]
# in those lines of code, it converts axis 0 and 1 to index and columns to make it easier to read
# 
# matplotlib is useful for data visualizations that can be static, animated, or interactive.
# import matplotlib.pyplot as plt #imports matplotlib
# import numpy as np #generates data for later use
# np.random.seed(444)
# 
# Plotly is good to use for interactive plots like contour plots, dendograms, and 3D charts
# import plotly.graph_objects as go
# 
# fig = go.Figure(
#     data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
#     layout=go.Layout(height=600, width=800)
# )
# 
# fig.layout.template = None # to slim down the output
# 
# print("Dictionary Representation of A Graph Object:\n\n" + str(fig.to_dict()))
# print("\n\n")
# print("JSON Representation of A Graph Object:\n\n" + str(fig.to_json()))
# print("\n\n")
