#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import json


# In[4]:


file_image=open('/Users/anandmohan.jhaoutlook.com/Downloads/YOLO_assignment.json')


# In[5]:


data = json.load(file_image)


# In[21]:


x=data.keys()
print(x)
y=data.values()
#print(y)
z=data.items()
print(f'{z}')


# In[14]:


print(x)


# In[22]:


for x, y in data.items():
  print(x, y)


# In[23]:


import pandas as pd
import numpy as np


# In[38]:


df = pd.DataFrame(data[x])


# In[26]:





# In[ ]:




