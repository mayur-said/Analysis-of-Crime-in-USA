import universal_functions
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://%s:%s@127.0.0.1" % ("dap", "dap"))
db = client['dap_project']

#Montgomery County
table_name = 'montgomery_county'
collection = db['montgomery_county']
i = 0
lst = []
for doc in collection.find():
    lst.append(doc)
    i += 1
    if i%30000 == 0:
        df = pd.DataFrame(lst)
        drop_cols = ['_id', 'incident_id', 'case_number', 'location', 'geolocation', ':@computed_region_tx5f_5em3', ':@computed_region_kbsp_ykn9',
       ':@computed_region_d7bw_bq6x', ':@computed_region_rbt8_3x7n',':@computed_region_a9cs_3ed7', ':@computed_region_r648_kzwt',
       ':@computed_region_d9ke_fpxt', ':@computed_region_vu5j_pcmz', 'end_date', 'street_prefix_dir', 'street_suffix_dir']
        df = df.drop(drop_cols, axis = 1)
        df = df.drop(df[df['crimename1'].isnull()].index)
        df = df.drop(df[df['district'] == "NaN"].index)

        df['start_date'] = pd.to_datetime(df['start_date'])
        df = df[df['start_date'] < '2022-01-01'].copy()
        df['week'] = df['start_date'].dt.day_of_week
        df['year'] = df['start_date'].dt.year
        df['month'] = df['start_date'].dt.month
        universal_functions.insert_into_postgres(df, table_name)
        lst = []
if lst:
    df = pd.DataFrame(lst)
    drop_cols = ['_id', 'incident_id', 'case_number', 'location', 'geolocation', ':@computed_region_tx5f_5em3', ':@computed_region_kbsp_ykn9',
                 ':@computed_region_d7bw_bq6x', ':@computed_region_rbt8_3x7n',':@computed_region_a9cs_3ed7', ':@computed_region_r648_kzwt',
                 ':@computed_region_d9ke_fpxt', ':@computed_region_vu5j_pcmz', 'end_date', 'street_prefix_dir', 'street_suffix_dir']
    df = df.drop(drop_cols, axis = 1)
    df = df.drop(df[df['crimename1'].isnull()].index)
    df = df.drop(df[df['crimename1'].isnull()].index)
    df = df.drop(df[df['district'] == "NaN"].index)

    df['start_date'] = pd.to_datetime(df['start_date'])
    df = df[df['start_date'] < '2022-01-01'].copy()
    df['week'] = df['start_date'].dt.day_of_week
    df['year'] = df['start_date'].dt.year
    df['month'] = df['start_date'].dt.month
    universal_functions.insert_into_postgres(df, table_name)

  

#LA Crimes
table_name = 'crime_reports'
collection = db['Los_Angeles_Crimes']
i = 0
lst = []
for doc in collection.find():
    lst.append(doc)

df = pd.DataFrame(lst)
drop_cols = ['_id', 'dr_no', 'part_1_2', 'mocodes', 'cross_street', 'crm_cd_2', 'crm_cd_3',
                'crm_cd_4', 'status', 'status_desc', 'rpt_dist_no', 'crm_cd_1']
df = df.drop(drop_cols, axis = 1)
#Renaming columns for better understanding
df.rename(columns={'date_rptd' : 'date_reported', 'date_occ' : 'date_occurred', 'time_occ' : 'time_occurred',
                'crm_cd' : 'crime_code', 'crm_cd_desc' : 'crime_description', 'vict_age' : 'victim_age',
                'vict_sex' : 'victim_sex', 'vict_descent' : 'victim_ethnicity', 'premis_cd' : 'premis_code',
                'premis_desc' : 'premis_description', 'weapon_used_cd' : 'weapon_used_code', 
                'weapon_desc' : 'weapon_description', 'lat' : 'latitude', 'lon' : 'longitude'}, inplace=True)
#Dropping the rows with missing values
df = df.dropna()
#Converting the columns to appropriate datatypes and setting the date format
df['date_occurred'] = pd.to_datetime(df['date_occurred'])
df['date_reported'] = pd.to_datetime(df['date_reported'])

df['date_occurred']= pd.to_datetime(df['date_occurred'], format= '%Y%m%d')
df['date_reported']= pd.to_datetime(df['date_reported'], format= '%Y%m%d')

df['time_occurred'] = df['time_occurred'].astype('int64')
df['area'] = df['area'].astype('int64')
df['crime_code'] = df['crime_code'].astype('int64')
df['victim_age'] = df['victim_age'].astype('int64')
df['premis_code'] = df['premis_code'].astype('int64')
df['weapon_used_code'] = df['weapon_used_code'].astype('int64')
df['latitude'] = df['latitude'].astype('float64')
df['longitude'] = df['longitude'].astype('float64')
universal_functions.insert_into_postgres(df, table_name)


#Call Of Service

table_name = 'ordersofservice'
collection = db['ordersofservice']
i = 0
lst = []
for doc in collection.find():
    lst.append(doc)
df = pd.DataFrame(lst)
drop_cols = [':@computed_region_m56f_hbma', ':@computed_region_sikx_bdeb', ':@computed_region_spev_d8jm',':@computed_region_u4yh_3wk9',
':@computed_region_k37d_then', ':@computed_region_ewbu_t8bu', ':@computed_region_evki_aju8', ':@computed_region_7fw3_kdpf', 
'timedispatch', 'timearrive', 'location']
df = df.drop(drop_cols, axis = 1)
df['timecreate']=pd.to_datetime(df.timecreate, format='%Y/%m/%d %H:%M') #converting to datetime
df['year'] = df['timecreate'].dt.year    #extracting the year colum
df['timecreate']= df['timecreate'].dt.strftime('%Y/%m/%d') #extracting only date 
#making sure all the variables are of string type for postgres
df[[ 'year', 'timecreate']] = df[['year','timecreate']].astype(str)
df = df.drop(["_id"], axis =1 ) #dropping the id colum generated by mongodb

#filtering for only crimes from the emergency list above and saving into a new df frame
l = ['HIT & RUN','ORAL SEXUAL BATTERY', 'SIMPLE ARSON DOMESTIC', 'CRIME AGAINST NATURE', 'PANDERING','UNLAWFUL SALES TO MINORS'
, 'SAFE BURGLARY', 'PANDERING', 'DESECRATION OF GRAVES', 'AGGRAVATED BATTERY BY CUTTING', 'HOMICIDE BY CUTTING', 'HIT & RUN FATALITY',
'CRIMINAL MISCHIEF DOMESTIC', 'SOLICITING FOR PROSTITUTION', 'HOMICIDE DOMESTIC', 'SIMPLE RAPE MALE VICTIM', 'ORAL SEXUAL BATTERY', 'HOSTAGE SITUATION','HIT & RUN CITY VEHICLE'
, 'UNDERAGE DRINKING VIOLATION','SIMPLE RAPE UNFOUNDED BY SPECIAL VICTIMS OR CHILD ABUSE', 'UNDERAGE DRINKING VIOLATION', 'FLOODED VEHICLE', 'SIMPLE RAPE UNFOUNDED BY SPECIAL VICTIMS OR CHILD ABUSE', 
'ARMED ROBBERY', 'MISDEMEANOR SEXUAL BATTERY', 'AGGRAVATED KIDNAPPING', 'SUICIDE ATTEMPT', 'SUICIDE THREAT' 'AGGRAVATED ARSON', 'POSSESSION OF STOLEN PROPERTY','AGGRAVATED BURGLARY', 'BLIGHTED PROPERTY', 
'SIMPLE ARSON', 'HOMICIDE', 'SIMPLE KIDNAPPING', 'ILLEGAL CARRYING OF WEAPON', 'ILLEGAL CARRYING OF WEAPON- GUN', 'ILLEGAL CARRYING OF WEAPON- KNIFE', 'UNCLASSIFIED DEATH',
'AGGRAVATED BATTERY BY KNIFE', 'AGGRAVATED RAPE MALE VICTIM', 'VIOLATION OF PROTECTION ORDER', 'CARJACKING- NO WEAPON', 'AUTO ACCIDENT POLICE VEHICLE''CARJACKING', 'THEFT BY EMBEZZLEMENT',
'AGGRAVATED ASSAULT DOMESTIC', 'DRIVING WHILE UNDER INFLUENCE', 'ABANDONED VEHICLE', 'ARMED ROBBERY WITH KNIFE', 'PICKPOCKET',
'SIMPLE ROBBERY, PROPERTY SNATCHING', 'FORGERY','EXTORTION (THREATS) DOMESTIC', 'AGGRAVATED CRIMINAL DAMAGE', 'HIT & RUN', 'PROSTITUTION', 'SEXUAL BATTERY' ]
df= df[df.typetext.isin(l)]
universal_functions.insert_into_postgres(df, table_name)
       
