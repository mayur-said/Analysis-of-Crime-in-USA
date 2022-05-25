import universal_functions
import config

#create database
create_database = f'CREATE DATABASE {config.postgres_database}'
universal_functions.create_database(create_database)



#Montgomery Crime Table

sql = '''
CREATE TABLE IF NOT EXISTS public.montgomery_county
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    offence_code text COLLATE pg_catalog."default",
    date text COLLATE pg_catalog."default",
    nibrs_code text COLLATE pg_catalog."default",
    victims integer,
    crimename1 text COLLATE pg_catalog."default",
    crimename2 text COLLATE pg_catalog."default",
    crimename3 text COLLATE pg_catalog."default",
    district text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    zip_code text COLLATE pg_catalog."default",
    agency text COLLATE pg_catalog."default",
    place text COLLATE pg_catalog."default",
    sector text COLLATE pg_catalog."default",
    beat text COLLATE pg_catalog."default",
    pra text COLLATE pg_catalog."default",
    address_number text COLLATE pg_catalog."default",
    address_street text COLLATE pg_catalog."default",
    street_type text COLLATE pg_catalog."default",
    start_date date,
    latitude text COLLATE pg_catalog."default",
    longitude text COLLATE pg_catalog."default",
    police_district_number text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    week text COLLATE pg_catalog."default",
    year text COLLATE pg_catalog."default",
    month text COLLATE pg_catalog."default",
    CONSTRAINT montgomery_county_pkey PRIMARY KEY (id)
)
'''

universal_functions.create_table(sql)


#LA crime_reports table
sql = '''

CREATE TABLE IF NOT EXISTS public.crime_reports
(
    date_reported timestamp without time zone,
    date_occurred timestamp without time zone,
    time_occurred text COLLATE pg_catalog."default",
    area text COLLATE pg_catalog."default",
    area_name text COLLATE pg_catalog."default",
    crime_code text COLLATE pg_catalog."default",
    crime_description text COLLATE pg_catalog."default",
    victim_age text COLLATE pg_catalog."default",
    victim_sex text COLLATE pg_catalog."default",
    victim_ethnicity text COLLATE pg_catalog."default",
    premis_code text COLLATE pg_catalog."default",
    premis_description text COLLATE pg_catalog."default",
    weapon_used_code text COLLATE pg_catalog."default",
    weapon_description text COLLATE pg_catalog."default",
    location text COLLATE pg_catalog."default",
    latitude text COLLATE pg_catalog."default",
    longitude text COLLATE pg_catalog."default",
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    CONSTRAINT crime_reports_pkey PRIMARY KEY (id)
)
'''

universal_functions.create_table(sql)

#orders of service table in postgres

sql = '''
CREATE TABLE IF NOT EXISTS public.ordersofservice
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nopd_item character(100) COLLATE pg_catalog."default" NOT NULL,
    type_ character varying(100) COLLATE pg_catalog."default",
    typetext character(100) COLLATE pg_catalog."default" NOT NULL,
    priority character(100) COLLATE pg_catalog."default" NOT NULL,
    initialtype character(100) COLLATE pg_catalog."default" NOT NULL,
    initialtypetext character(100) COLLATE pg_catalog."default" NOT NULL,
    initialpriority character(100) COLLATE pg_catalog."default" NOT NULL,
    mapx character(100) COLLATE pg_catalog."default" NOT NULL,
    mapy character(100) COLLATE pg_catalog."default" NOT NULL,
    timecreate character(100) COLLATE pg_catalog."default" NOT NULL,
    timeclosed character(100) COLLATE pg_catalog."default" NOT NULL,
    disposition character(100) COLLATE pg_catalog."default" NOT NULL,
    dispositiontext character(100) COLLATE pg_catalog."default" NOT NULL,
    selfinitiated character(100) COLLATE pg_catalog."default" NOT NULL,
    beat character(100) COLLATE pg_catalog."default" NOT NULL,
    block_address character(100) COLLATE pg_catalog."default" NOT NULL,
    zip character(100) COLLATE pg_catalog."default" NOT NULL,
    policedistrict character(100) COLLATE pg_catalog."default" NOT NULL,
    year character varying(100) COLLATE pg_catalog."default" NOT NULL
)
'''
universal_functions.create_table(sql)
