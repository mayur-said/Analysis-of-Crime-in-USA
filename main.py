import os  

os.system('python data_extraction.py')
os.system('python create_database_tables.py')
os.system('python data_preprocessing.py')
os.system('python Montgomery_Crime.py')