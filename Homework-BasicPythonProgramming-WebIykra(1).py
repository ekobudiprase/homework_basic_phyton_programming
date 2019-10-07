#!/usr/bin/env python
# coding: utf-8

# ### Homework Basic Python Programming

# **Eko Budi Prasetyo / 89170**

# **1. In the dataset of googleplaystore.csv, it consists of**

# In[5]:


import numpy as np
import pandas as pd

google_play_apps = pd.read_csv('dataset/googleplaystore.csv', encoding="latin1")
google_play_apps.shape


# In[6]:


google_play_apps.head()


# **Normalizing the data**

# In[7]:


google_play_apps.iloc[10472,1:] = google_play_apps.iloc[10472,1:].shift(1)


# **2. How many unique apps categories reflected in the dataset?**

# In[8]:


print("Unique apps categories : ", google_play_apps['Category'].nunique())
print(google_play_apps['Category'].value_counts())


# **3. How many unique genres according to the dataset?**

# In[9]:


print("Unique genres : ", google_play_apps['Genres'].nunique())
print(google_play_apps['Genres'].value_counts())


# **4. Which code is appropriate to drop duplicate values in 'App' column and remove its rows in Python?  Assume dataset was loaded as a pandas data frame variable: google_play_apps.**

# In[10]:


google_play_apps.drop_duplicates(subset='App', inplace=True)
google_play_apps.shape


# **5. Upon removing duplicate of App column, please run the following code to remove a row that contain 'Free' value at the 'Installs' column.**

# In[11]:


google_play_apps['Installs'] = google_play_apps['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)


# In[12]:


google_play_apps['Installs'] = google_play_apps['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)


# **6. If you want to convert data type of 'Installs' columns into integer, you can run the following code.**

# In[13]:


google_play_apps['Installs'] = google_play_apps['Installs'].astype(int)


# **7. Match Apps and Category based on provided dataset!**

# In[16]:


arr_app = [
    'WhatsApp Messenger',
    'FIFA Soccer', 
    'Flipboard: News For Our Time',
    'DU Battery Saver - Battery Charger & Battery Life', 
    'Dropbox', 
    'Subway Surfers', 
    'Pinterest', 
    'File Commander - File Manager/Explorer'
]
google_play_apps.loc[google_play_apps['App'].isin(arr_app)].filter(['App','Category'])


# **8. The following applications were installed by more than 1 billion users, EXCEPT**

# In[18]:


google_play_apps.loc[google_play_apps['Installs'] >= 1000000000].filter(['App'])


# **9. Arrange top COMMUNICATION category apps from the highest number of reviews to the lowest!**

# In[30]:


google_play_apps['Reviews'] = google_play_apps['Reviews'].astype(int)
google_play_apps.loc[google_play_apps['Category'].isin(['COMMUNICATION'])].sort_values(['Reviews'],ascending=False).filter(['App','Reviews'])


# **10. Arrange top 3 game category apps based on number of installed and rating!**

# In[29]:


google_play_apps['Rating'] = google_play_apps['Rating'].astype(float)
google_play_apps.loc[google_play_apps['Category'].isin(['GAME'])].sort_values(['Installs','Rating'],ascending=False).head(3).filter(['App','Category','Rating','Installs'])

