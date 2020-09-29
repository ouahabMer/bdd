__author__ = 'Rashed'

#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys

conn = psycopg2.connect("host='localhost' dbname='movie_db' user='postgres' password='admin'")
cursor = conn.cursor()

TABLES = {}
TABLES['movies'] = (
    "CREATE TABLE movies("
    "id INTEGER PRIMARY KEY NOT NULL,"
    "title VARCHAR(200) NOT NULL,"
    "geners VARCHAR (200) NOT NULL )")

TABLES['links'] = (
    "CREATE TABLE links("
    "movieid INTEGER NOT NULL,"
    "imdbid INTEGER  NOT NULL,"
    "tmdbid INTEGER  NOT NULL)")


TABLES['ratings'] = (
    "CREATE TABLE ratings("
    "userid INTEGER PRIMARY KEY NOT NULL,"
    "movieid INTEGER NOT NULL,"
    "ratings VARCHAR(200) NOT NULL,"
    "timestapm VARCHAR (200) NOT NULL )")


TABLES['tags'] = (
    "CREATE TABLE tags("
    "userid INTEGER PRIMARY KEY NOT NULL,"
    "movieid INTEGER NOT NULL,"
    "tags VARCHAR (200) NOT NULL,"
    "timestamp VARCHAR (200) NOT NULL)")

for name, ddl in TABLES.items():
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)

conn.commit()
