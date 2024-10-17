#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path_latest = 'USvideos.csv'
data = pd.read_csv(file_path_latest)

# Set the style for seaborn plots
sns.set(style="whitegrid")

# Task 1: Distribution of variables (views, likes, dislikes, and comment counts)
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Distribution of Views
sns.histplot(data['views'], bins=50, kde=True, ax=axs[0, 0], color='blue')
axs[0, 0].set_title('Distribution of Views')

# Distribution of Likes
sns.histplot(data['likes'], bins=50, kde=True, ax=axs[0, 1], color='green')
axs[0, 1].set_title('Distribution of Likes')

# Distribution of Dislikes
sns.histplot(data['dislikes'], bins=50, kde=True, ax=axs[1, 0], color='red')
axs[1, 0].set_title('Distribution of Dislikes')

# Distribution of Comment Count
sns.histplot(data['comment_count'], bins=50, kde=True, ax=axs[1, 1], color='purple')
axs[1, 1].set_title('Distribution of Comment Count')

plt.tight_layout()
plt.show()


# In[17]:


# Task 2: Detect Outliers using Box Plots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Box Plot for Views
sns.boxplot(data['views'], ax=axs[0, 0], color='blue')
axs[0, 0].set_title('Box Plot of Views')

# Box Plot for Likes
sns.boxplot(data['likes'], ax=axs[0, 1], color='green')
axs[0, 1].set_title('Box Plot of Likes')

# Box Plot for Dislikes
sns.boxplot(data['dislikes'], ax=axs[1, 0], color='red')
axs[1, 0].set_title('Box Plot of Dislikes')

# Box Plot for Comment Count
sns.boxplot(data['comment_count'], ax=axs[1, 1], color='purple')
axs[1, 1].set_title('Box Plot of Comment Count')

plt.tight_layout()
plt.show()


# In[14]:


# Task 3: Correlation between numerical variables (views, likes, dislikes, comment count)
# Creating a correlation heatmap
plt.figure(figsize=(8,6))
corr_matrix = data[['views', 'likes', 'dislikes', 'comment_count']].corr()

# Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# In[ ]:




