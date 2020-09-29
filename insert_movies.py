__author__ = 'Rashed'
#!/usr/bin/python3
import psycopg2
import csv

connection = psycopg2.connect("host='localhost' dbname='movie_db' user='postgres' password='admin'")
mycursor = connection.cursor()

def insert_movies():
    with open('./data/movies.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO movies(id,title, geners) VALUES ('%s', '%s', '%s' );" % (row[0], row[1], row[2])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()


def insert_links():
    with open('./data/links.csv', newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO links (movieid,imdbid, tmdbid) VALUES ('%s','%s', '%s');" % (row[0], row[1], row[2])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()


def insert_ratings():
    with open('./data/ratings.csv', newline='',  encoding="utf8") as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO ratings(userid,movieid, ratings,timestapm) VALUES ('%s','%s', '%s', '%s' );" % (row[0], row[1], row[2], row[3])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()


def insert_tags():
    with open('./data/tags.csv', newline='',  encoding="utf8") as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO tags(userid,movieid, tags,timestamp) VALUES ('%s','%s', '%s', '%s' );" % (row[0], row[1], row[2], row[3])
            print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               # Commit your changes in the database
               connection.commit()
            except:
               # Rollback in case there is any error
               connection.rollback()



insert_movies()
insert_links()
insert_ratings()
insert_tags()
# disconnect from server
connection.close()