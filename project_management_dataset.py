# -*- coding: utf-8 -*-
"""Project_Management_Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10m5zq-dhLtJmZRkvMvVAXKFuUpKbPlyD

<h1><b>PROJECT MANAGEMENT DATASET</h1>
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""(1) LOADING DATASET"""

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('/content/ProjectManagement.csv')
print(df.head())
print(df.tail())

"""

> *Checking datatypes*

"""

print(df.dtypes)

"""
> *Checking for null values*"""

print(df.isnull().sum())

"""

> Add blockquote

"""

df.describe()

sns.histplot(data=df,x=" Project Cost ",kde=True)
plt.title("Distribution of Project Costs")
plt.show()

"""KEY PERFORMANCE INDICATORS(KPIs)
=> To test business understanding they mostly ask about KPIs in the interview
=>To measure the performance we use KPIs

> ***Project count by type***
"""

sns.countplot(data=df,x="Project Type")
plt.xticks(rotation=45)
plt.title('Project Count By Type')
plt.show()

"""

> KPI
  ***Black line - indicates the starting and ending point***

"""

sns.barplot(data=df,x='Department',y=' Project Cost ',estimator=np.mean)
plt.xticks(rotation=90)
plt.title('Average Cost By Department')
plt.show()

"""

> ***Using Pie chart to see the Project Status Distribution***

"""

plt.pie(df['Status'].value_counts(),labels=df['Status'].value_counts().index,autopct='%1.1f%%')
plt.title('Project Status Distribution')
plt.show()





"""



>*** Correlation***


"""

df1 = df[['Year','Month']]
corr= df1.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""

> ***Boxplot - Project Completion % by Complexity***

"""

sns.boxplot(data=df,x='Complexity',y='Completion%',showfliers=False)
plt.title('Project Completion% by Complexity')
plt.show()

"""

> ***Time Series Analysis***

"""

df[' Project Cost '] = df[' Project Cost '].str.replace(',', '').astype(float)

df['Year-Month']=df['Year'].astype(str) +'-'+ df['Month'].astype(str)
df.groupby('Year-Month')[' Project Cost '].sum().plot()
plt.title('Monthly Project Costs Over Time')
plt.xticks(rotation=45)
plt.show()

sns.scatterplot(data=df, x=' Project Cost ', y=' Project Benefit ')
plt.title('Project Cost vs Benifit')
plt.show()

"""

>***3D plot***
"""

import plotly.express as px

fig = px.scatter_3d(df, x=' Project Cost ', y=' Project Benefit ', z='Complexity',
                  color='Project Type')
fig.update_layout(scene = dict(
                    xaxis = dict(title  = 'Project Cost'),
                    yaxis = dict(title  = 'Project Benefit'),
                    zaxis = dict(title  = 'Complexity')))
fig.show()



complexity_mapping = {'low': 1, 'medium': 2, 'high': 3}
df['Complexity'] = df['Complexity'].map(complexity_mapping)
# Create the 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df[' Project Cost '], df[' Project Benefit '], df['Complexity'])
ax.set_xlabel('Project Cost')
ax.set_ylabel('Project Benefit')
ax.set_zlabel('Complexity')
plt.title("3D Chart of Cost, Benefit, and Complexity")
plt.show()