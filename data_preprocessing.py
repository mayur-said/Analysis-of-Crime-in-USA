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
