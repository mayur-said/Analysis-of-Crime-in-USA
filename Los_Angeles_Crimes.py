import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import universal_functions

#query data from postgres
table_name = 'crime_reports'
df = universal_functions.read_data_from_postgres(table_name)

#1st visualization
#when were most crimes were commited
crime = df[['date_occurred','crime_description']]
crime = crime.groupby('date_occurred').count().reset_index(drop=False)
crime.columns = ['date_occurred', 'Counts']
fig = px.line(crime, x='date_occurred',y='Counts',title='Number of Crimes in Los Angeles')
fig.show()


#2nd visualization
#Top most frequent and major crimes
def bar(categories,x,y,color,title,xlab,ylab):
    fig = px.bar(categories, x=x, y=y,
             color=color,
             height=600)
    fig.update_layout(
    title_text=title, 
    xaxis_title_text=xlab, 
    yaxis_title_text=ylab,
    bargap=0.2, 
    bargroupgap=0.1
    )
    fig.show()
    
Number_crimes = df['crime_description'].value_counts()
values = Number_crimes.values
categories = pd.DataFrame(data=Number_crimes.index, columns=["crime_description"])
categories['values'] = values

bar(categories,categories['crime_description'][0:10],categories['values'][0:10]
    ,categories['crime_description'][0:10],'Top 10 Major Crimes in Los Angeles','Crime','Count')


#3rd visualization
#Victim gender by crimes
# Removing Entries for X and H and - (by elimination)
df["Victim Gender"] = df["victim_sex"][df["victim_sex"] != "X"]
df["Victim Gender"] = df["Victim Gender"][df["Victim Gender"] != "H"]
df["Victim Gender"] = df["Victim Gender"][df["Victim Gender"] != "-"]

# Combining two columns into a dataframe
cc_vg = df[["crime_description", "Victim Gender"]]
# Dropping null values
cc_vg = cc_vg[pd.notnull(cc_vg["Victim Gender"])]

# Saving top 10 crimes
crimetop10 = cc_vg["crime_description"].value_counts().head(10).index
# Choosing data that is included in the top 10 crimes (by selection)
crimecc = cc_vg.loc[cc_vg["crime_description"].isin(crimetop10)]

# Group by Crime Description and Victim Gender
cc_gender = crimecc.groupby(["crime_description", "Victim Gender"]).size().reset_index(name="Count")

# Factorplot Crime and Gender based on count
ax = sns.catplot(x="crime_description", hue="Victim Gender", kind="count", data=crimecc, height=7, aspect=3, 
                    palette=["red", "blue"])

plt.title("Victim Gender by Crime")
ax.set_xticklabels(rotation=-90)
ax.set_xlabels("Victim of Crime")
ax.set_ylabels("Count")
sns.despine()


#4th visualization
#Number of crimes according to area name
fig,ax = plt.subplots(figsize=(12,5))
sns.countplot(y="area_name",data=df,palette='bright',alpha=0.75)
ax.set_title('Crime in LA (2020 - Present) by Area');


#5th visualization
#Victims ethnicity 
plt.style.use('ggplot')
plt.title('Victims Categorization by Ethnicity')
plt.xlabel('Victim Ehnicity')
plt.ylabel('Crime Counts')
color=plt.cm.Pastel2(np.linspace(0,4,10))
df["victim_ethnicity"].value_counts()[:8].plot.bar(figsize=(12,8))
plt.show()
