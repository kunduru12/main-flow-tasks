#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv("heart.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.columns.values


# In[7]:


df.isna().sum()


# In[8]:


df.info()


# In[9]:


df.hist(bins=100,grid=True,figsize=(20,15));


# In[10]:


df.describe()


# In[11]:


questions=["1.how many people have heart disease and how many people dosen't have heart disease?",
          "2.people of which sex has most heart disease?",
          "3.people of which sex has which type of chest pain most?",
          "4.people with which chest pain are most pron to have disease?"]


# In[12]:


questions


# In[13]:


#first question answer
#1.how many people have heart disease and how many people dosen't have heart disease?
#getting the values
df.target.value_counts()


# In[14]:


#ploting bar chart
df.target.value_counts().plot(kind='bar',color=["orchid","salmon"])
plt.title("Heart disease values")
plt.xlabel("1=Heart disease,0=no heart disease")
plt.ylabel("amount");


# In[15]:


#plotting pie chart
df.target.value_counts().plot(kind='pie',figsize=(8,6))
plt.legend(["disease","no disease"]);


# In[16]:


# '0' represent "female"
#'1' represent "male"
#sex column part
#'0' represent'no disease'
#'1' represent'disease'
# target column part
#now let's check how many male and femaleare in the dataset
df.sex.value_counts()


# In[17]:


#ploting a pie chart
df.sex.value_counts().plot(kind='pie',figsize=(8,6))
plt.title('Male Female ratio')
plt.legend(['Male','female']);


# In[18]:


#lets find answer for 2nd question
#2.people of which sex has most heart disease?
pd.crosstab(df.target,df.sex)


# In[19]:


sns.countplot(x='target',data=df,hue='sex')
plt.title('Heart disease frequency for sex')
plt.xlabel("0=no heart disease,1 =heart disease");


# In[20]:


#number of male is more than double in our dataset than female
#more than 45% male has heart disease and 75% female has heart disease


# In[21]:


#lets move to 3rd quetion
#3.people of which sex has which type of chest pain most?
#counting values for different chest pain
df.cp.value_counts()


# In[22]:


#ploting a bar chart
df.cp.value_counts().plot(kind='bar',color={'salmon','lightskyblue','springgreen','khaki'})
plt.title("chest pain type vs count")


# In[23]:


pd.crosstab(df.sex,df.cp)


# In[24]:


pd.crosstab(df.sex,df.cp).plot(kind='bar',color={'salmon','lightskyblue','springgreen','khaki'})
plt.title("type of chest pasin for sex")
plt.xlabel('0=female,1=male');


# In[25]:


#now question 4
#4.people with which chest pain are most pron to have disease?
pd.crosstab(df.cp,df.target)


# In[26]:


sns.countplot(x='cp',data=df,hue='target');


# In[27]:


#most of people who has type 0 chest pain has less chance of heart disease.
#and we see the opposite for other types
#now lets take look at our age column
#create a distribution plot with normal distribution curve
sns.displot(x='age',data=df,bins=30,kde=True);


# In[28]:


sns.displot(x='thalach',data=df,bins=30,kde=True, color='red');


# In[ ]:




