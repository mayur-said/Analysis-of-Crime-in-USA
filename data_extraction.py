import universal_functions

#Read  and Insert Montgomery Data
source = 'data.montgomerycountymd.gov'
dataset_identifier = 'icn6-v9z3'
collection = 'montgomery_county'
universal_functions.read_insert_data_mongodb(source, dataset_identifier, collection)
