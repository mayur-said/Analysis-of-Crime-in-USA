import json
from urllib.request import urlopen
from sodapy import Socrata
from pymongo import MongoClient
import psycopg2
import psycopg2.extras as extras
import pandas.io.sql as sqlio
import config

client = MongoClient("mongodb://%s:%s@127.0.0.1" % ('dap', 'dap'))
db = client['dap_project']

def read_insert_data_mongodb(source, dataset_identifier, collection_name):
    try:
        lst = []
        i = 0
        with Socrata(source, None) as client:
            #read data
            results = client.get_all(dataset_identifier)
            for res in results:
                lst.append(res)
                i+= 1
                if i%20000 == 0:
                    collection = db[collection_name]
                    collection = collection.insert_many(lst)
                    if collection:
                        print(f'{i} entries inserted succesfully')
                    lst = []
            if lst:
                collection = db[collection_name]
                collection = collection.insert_many(lst)
    except Exception as e:
        print('Error',e)


def create_database(create_database):
    try:
        dbConnection = psycopg2.connect(
            user = 'postgres',
            password = '1234',
            host = "localhost",
            port = "5432",
            database = "postgres")
        dbConnection.set_isolation_level(0)
        dbCursor = dbConnection.cursor()
        query = create_database
        dbCursor.execute(query)
        print("Query Executed successfully........")
        dbCursor.close()
    except (Exception , psycopg2.Error) as dbError:
        print("Error: %s" % dbError)
        dbCursor.close()


def create_table(create_query):
    try:
        dbConnection = psycopg2.connect(
            user = config.postgres_username,
            password = config.postgres_password,
            host = "localhost",
            port = "5432",
            database = config.postgres_database)
        dbCursor = dbConnection.cursor()
        create_query = create_query
        dbCursor.execute(create_query)
        dbConnection.commit()
        print("Table created successfully........")
        dbCursor.close()
    except (Exception , psycopg2.Error) as dbError:
        print("Error: %s" % dbError)
        dbCursor.close()


def insert_into_postgres(df, table_name):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    query = f"INSERT INTO {table_name}({cols}) VALUES %s"
    try:
        dbConnection = psycopg2.connect(
            user = config.postgres_username,
            password = config.postgres_password,
            host = "localhost",
            port = "5432",
            database = config.postgres_database)
        dbCursor = dbConnection.cursor()
        extras.execute_values(dbCursor, query, tuples)
        dbConnection.commit()
        print('Data Inserted Successfully')
        dbCursor.close()
    except (Exception , psycopg2.Error) as dbError:
        print("Error: %s" % dbError)
        dbConnection.rollback()
        dbCursor.close()

def read_data_from_postgres(table_name):
    query = f'select * from {table_name} order by id'
    try:
        dbConnection = psycopg2.connect(
            user = config.postgres_username,
            password = config.postgres_password,
            host = "localhost",
            port = "5432",
            database = config.postgres_database)
        dbCursor = dbConnection.cursor()
        df = sqlio.read_sql_query(query, dbConnection)
        dbCursor.close()
        return df
    except (Exception , psycopg2.Error) as dbError:
        print("Error: %s" % dbError)
        dbCursor.close()
