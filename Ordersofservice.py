#Importing necessary packages for the visualisation
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import universal_functions

#query data from postgres
table_name = 'ordersofservice'
crime_data = universal_functions.read_data_from_postgres(table_name)

#visualization

#plot of each year and the amount of crime reports they each got
year = crime_data.groupby('year')['nopd_item'].count()
plt.figure(figsize = (10,5))
year = crime_data.groupby('year')['nopd_item'].size().reset_index(name='counts')
sns.barplot(x = 'year', y = 'counts', data = year, palette='bright')
plt.xticks(rotation = 45)
plt.show()

#the amount of different crimes that was reported through the emergency lines
plt.figure(figsize = (10,5))
new = crime_data.groupby('year')['typetext'].nunique().reset_index(name='counts')
sns.barplot(x = 'year', y = 'counts', data = new, palette='bright')
plt.title('Numbers of different crimes reported per year')
plt.xticks(rotation = 45)
plt.show()

#Plot of 51 different crimes and the amount of report each of them have
plt.figure(figsize = (15,5))
df_sorted=crime_data.groupby(['typetext'])['nopd_item'].size().reset_index(name='counts')
tmp = df_sorted.sort_values('counts', ascending = False, ignore_index=True)
sns.barplot(x = 'typetext', y = 'counts', data = tmp[:16], palette='bright')
plt.title('Top 15 Crimes and their Occurence Between 2020-2021')
plt.xticks(rotation = 45)
plt.show()

#total amount of self initiated crimes or not
crime_data["selfinitiated"].value_counts().plot.pie(autopct ='%.2f')

#to check which crime was self initiated or not
fig = px.box(crime_data, x="typetext", y="year", color='selfinitiated')
fig.show()


#the piority of each crime, notice where 2 means higher priority and A is highest piority year
#notice how most hit and run are not high priority
plt.figure(figsize = (15,5))
tmp =crime_data.groupby(["initialpriority", 'typetext'])['nopd_item'].size().reset_index(name='counts')
tmp = tmp.sort_values('counts', ascending = False, ignore_index=True).iloc[:21]
tmp["new"] = tmp['initialpriority'].astype(str).apply(lambda x: x[:2]) +","+ tmp['typetext'].astype(str)
sns.barplot(x = 'new', y = 'counts', data = tmp, palette='bright')
plt.title('Top 15 Crimes and their Occurence Between 2020-2021')
plt.xticks(rotation = 45)
plt.show()

