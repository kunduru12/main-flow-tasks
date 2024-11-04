#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_excel('diabetes.xlsx')
data.head(5)


# In[2]:


data.tail(4)


# In[3]:


type(data)


# In[4]:


data.shape


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data = data.drop_duplicates()
data


# In[8]:


data.isnull()


# In[9]:


data.isnull().sum()


# In[10]:


data.isnull().sum().sum()


# In[11]:


import numpy as np
from scipy import stats


# In[12]:


data.columns


# In[13]:


data.drop(['PatientID', 'Gender', 'Ethnicity', 'SocioeconomicStatus',
'EducationLevel', 'Smoking', 'AlcoholConsumption',
'FamilyHistoryDiabetes', 'GestationalDiabetes',
'PolycysticOvarySyndrome', 'PreviousPreDiabetes',
'Hypertension', 'AntihypertensiveMedications',
'Statins', 'AntidiabeticMedications', 'FrequentUrination',
'ExcessiveThirst', 'UnexplainedWeightLoss',
'BlurredVision', 'SlowHealingSores', 'TinglingHandsFeet',
'HeavyMetalsExposure', 'OccupationalExposureChemicals',
'WaterQuality', 'Diagnosis', 'DoctorInCharge'],
axis=1, inplace=True)
print(data.head())


# In[14]:


Q1=data.quantile(0.25)
Q3=data.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[15]:


data[~((data< (Q1-1.5*IQR) ) | (data>(Q3+1.5*IQR)) ) .any(axis=1)]
data


# In[16]:


data.describe()


# In[17]:


print(data.columns)


# In[19]:


'''
Questions
1. What is the overall distribution of ages in the dataset?,
2. What is the distribution of BMI values among the participants?,
3. How does physical activity level correlate with BMI?,
4. Are there trends in physical activity levels across different age groups?,
5. What are the average systolic and diastolic blood pressure readings across different age groups?,
6. Are there patterns in fasting blood sugar levels based on BMI and age?,
7. How do total cholesterol, LDL, HDL, and triglycerides compare among different age groups?,
'''


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[22]:


# What is the overall distribution of ages in the dataset?
plt.figure(figsize=(6, 6))
sns.histplot(data['Age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[24]:


# What is the distribution of BMI values among the participants?
data['AgeGroup'] = pd.cut(data['Age'], bins=[20, 30, 40, 50, 60, 70],
labels=['20-30', '30-40', '40-50', '50-60', '60-70'])
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='AgeGroup', y='BMI')
plt.title('BMI by Age Group')
plt.xlabel('Age Group')
plt.ylabel('BMI')
plt.show()


# In[25]:


print(data[['PhysicalActivity', 'BMI', 'SystolicBP', 'DiastolicBP']].describe())
print(data[['PhysicalActivity', 'BMI', 'SystolicBP', 'DiastolicBP']].nunique())


# In[26]:


# How does physical activity level correlate with BMI or health metrics like␣
get_ipython().set_next_input('↪blood pressure');get_ipython().run_line_magic('pinfo', 'pressure')
# Scatter Plot for Physical Activity vs. BMI
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='PhysicalActivity', y='BMI',
hue='PhysicalActivity', palette='viridis', s=100)
plt.title('Physical Activity Level vs. BMI')
plt.xlabel('Physical Activity Level')
plt.ylabel('BMI')
plt.grid()
plt.show()


# In[28]:


# How does physical activity level correlate with BMI or health metrics like blood pressure?
# Calculating and printing correlation coefficient for Physical Activity and BMI
correlation_bmi = data['PhysicalActivity'].corr(data['BMI'])
print(f'Correlation between Physical Activity and BMI: {correlation_bmi:.2f}')


# In[29]:


pd.crosstab(data.PhysicalActivity, data.AgeGroup)


# In[32]:


#Are there trends in physical activity levels across different age groups?
# Creating age groups
bins = [18, 25, 35, 45, 55, 65, 75, 85]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76+']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
# Calculating average physical activity level by age group
avg_activity_by_age = data.groupby('AgeGroup')['PhysicalActivity'].mean().reset_index()
# Bar Plot for Average Physical Activity by Age Group
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_activity_by_age, x='AgeGroup', y='PhysicalActivity',palette='viridis')
plt.title('Average Physical Activity Level by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Physical Activity Level')
plt.show()


# In[33]:


pd.crosstab(data.AgeGroup, data.SystolicBP)


# In[34]:


pd.crosstab(data.AgeGroup, data.DiastolicBP)


# In[35]:


# What are the average systolic and diastolic blood pressure readings across different age groups?
# Creating age groups
bins = [18, 25, 35, 45, 55, 65, 75, 85]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76+']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
# Calculating average systolic and diastolic blood pressure by age group
avg_bp_by_age = data.groupby('AgeGroup')[['SystolicBP', 'DiastolicBP']].mean().reset_index()


# In[36]:


# Bar Plot for Average Systolic Blood Pressure
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.barplot(data=avg_bp_by_age, x='AgeGroup', y='SystolicBP', palette='Blues')
plt.title('Average Systolic Blood Pressure by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Systolic BP')
plt.tight_layout()
plt.show()


# In[37]:


# Bar Plot for Average Diastolic Blood Pressure
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 2)
sns.barplot(data=avg_bp_by_age, x='AgeGroup', y='DiastolicBP', palette='Reds')
plt.title('Average Diastolic Blood Pressure by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Diastolic BP')
plt.tight_layout()
plt.show()


# In[38]:


#Are there patterns in fasting blood sugar levels based on BMI and age?
# Scatter Plot for Fasting Blood Sugar vs. BMI
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='BMI', y='FastingBloodSugar', hue='Age',palette='viridis', s=100)
plt.title('Fasting Blood Sugar vs. BMI')
plt.xlabel('BMI')
plt.ylabel('Fasting Blood Sugar (mg/dL)')
plt.grid()
plt.show()


# In[39]:


correlation_bmi = data['FastingBloodSugar'].corr(data['BMI'])
print(f'Correlation between Fasting Blood Sugar and BMI: {correlation_bmi:.2f}')


# In[40]:


#Are there patterns in fasting blood sugar levels based on BMI and age?
# Scatter Plot for Fasting Blood Sugar vs. Age
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Age', y='FastingBloodSugar', hue='BMI',palette='plasma', s=100)
plt.title('Fasting Blood Sugar vs. Age')
plt.xlabel('Age')
plt.ylabel('Fasting Blood Sugar (mg/dL)')
plt.grid()
plt.show()


# In[41]:


correlation_age = data['FastingBloodSugar'].corr(data['Age'])
print(f'Correlation between Fasting Blood Sugar and Age: {correlation_age:.2f}')


# In[42]:


# How do total cholesterol, LDL, HDL, and triglycerides compare among different␣age groups?
# Creating age groups
bins = [18, 25, 35, 45, 55, 65, 75, 85]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66-75', '76+']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)


# In[43]:


# Calculating average lipid levels by age group
avg_lipidlevels = data.groupby('AgeGroup')[['CholesterolTotal','CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides']].mean().reset_index()


# In[45]:


#How do total cholesterol, LDL, HDL, and triglycerides compare among different␣age groups?
# Bar Plot for Average Lipid Levels
plt.figure(figsize=(14, 8))
avg_lipidlevels.plot(x='AgeGroup', kind='bar', figsize=(14, 8), legend=True)
plt.title('Average Lipid Levels by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Levels')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.legend(title='Lipid Type')
plt.tight_layout()
plt.show()


# In[ ]:




