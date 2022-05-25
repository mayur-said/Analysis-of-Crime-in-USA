import os  

os.system('python data_extraction.py')
os.system('python create_database_tables.py')
os.system('python data_preprocessing.py')
os.system('python Montgomery_Crime.py')
os.system('python Los_Angeles_Crimes.py')
os.system('python Ordersofservice.py')