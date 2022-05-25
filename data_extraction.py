import universal_functions

#Read  and Insert Montgomery Data
source = 'data.montgomerycountymd.gov'
dataset_identifier = 'icn6-v9z3'
collection = 'montgomery_county'
universal_functions.read_insert_data_mongodb(source, dataset_identifier, collection)

#Read and Insert Call of Service Data
source = 'data.nola.gov'               #datasource
dataset_identifier = 'hp7u-i9hf'       #identifier
collection = 'ordersofservice'
universal_functions.read_insert_data_mongodb(source, dataset_identifier, collection)

source = 'data.nola.gov'
dataset_identifier = '3pha-hum9'
collection = 'ordersofservice'
universal_functions.read_insert_data_mongodb(source, dataset_identifier, collection)

#Reading and Inserting Los Angeles Crime Data
source = 'data.lacity.org'
dataset_identifier = '2nrs-mtv8'
collection = 'Los_Angeles_Crimes'
universal_functions.read_insert_data_mongodb(source, dataset_identifier, collection)
