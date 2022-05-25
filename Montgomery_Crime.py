import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
import universal_functions
sns.color_palette('bright')

#query data from postgres
table_name = 'montgomery_county'
df = universal_functions.read_data_from_postgres(table_name)

#Visualization
df['start_date'] = pd.to_datetime(df['start_date'])
df["month"] = pd.to_numeric(df["month"])
df["year"] = pd.to_numeric(df["year"])
df["week"] = pd.to_numeric(df["week"])
df_month_week = df.groupby(['month', 'week']).size().reset_index(name='counts')
df_year = df.groupby(['year']).size().reset_index(name='counts')
df_victim = df.groupby(['year'])['victims'].sum().reset_index(name='victims')

#Plot for Crimes Reported per Week
plt.figure(figsize = (10,5))
ax = sns.lineplot(x = 'week', y = 'counts', hue = 'month', data = df_month_week, palette='bright')
ax.set
plt.xticks(ticks = [0, 1, 2, 3, 4, 5, 6], 
           labels = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday'] ,rotation = 45)
plt.show()

#Plot for Crime Reported Each Year
plt.figure(figsize = (10,5))
plt.plot(df_year['year'], df_year['counts'], marker='o')
plt.xticks(rotation = 45)
plt.show()

#Plot for Total Victims Each Year
plt.figure(figsize = (10,5))
plt.plot('year', 'victims', data = df_victim, marker='o')
plt.xticks(rotation = 45)
plt.xlabel('Year')
plt.ylabel('Total Victims')
plt.show()

#Crime Reported in Top 10 Cities
plt.figure(figsize = (10,5))
sns.countplot(y="city", data=df,
              order=df.city.value_counts().iloc[:10].index)
plt.xticks(rotation = 45)
plt.show()

crime_list1 = ['Aggravated Assault']
new_df1 = df[df['crimename2'].isin(crime_list1)]
new_df_year = new_df1.groupby(['year', 'crimename2']).size().reset_index(name='counts')

#Plot for Reported Crime classified as Aggravated Assault Each Year
plt.figure(figsize = (10,5))
plt.plot(new_df_year['year'], new_df_year['counts'], marker='o')
plt.xticks(rotation = 45)
plt.show()

#Plot for Top 10 Cities for Reported Crime classified as Aggravated Assault
plt.figure(figsize = (10,5))
sns.countplot(y="place", data=new_df1,
              order=new_df1.place.value_counts().iloc[:10].index)
plt.xticks(rotation = 45)
plt.show()



