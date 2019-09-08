import sqlite3
import mysql.connector
import pymongo

class QuotePipeline(object):
    def process_item(self, item, spider):
        print('Pipeline: ' + item['author'][0])
        return item


class SqlitePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('quotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        print('Initialize database')
        self.curr.execute('DROP TABLE IF EXISTS quotes')
        self.curr.execute('CREATE TABLE quotes (text text, author text, tags text)')

    def store_to_db(self, item):
        self.curr.execute('INSERT INTO quotes VALUES (?, ?, ?)', (item['text'][0], item['author'][0], item['tags'][0]))
        self.conn.commit()

    def process_item(self, item, spider):
        print('Pipeline: Save item to SQLite database')
        self.store_to_db(item)
        return item


class MySQLPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_data_base()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port='9002',
            user='root',
            password='example'
        )

    def create_data_base(self):
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE DATABASE IF NOT EXISTS scrapy")
        self.curr.execute('USE scrapy')

    def create_table(self):
        self.curr.execute('CREATE TABLE IF NOT EXISTS quotes (text TEXT, author VARCHAR(20), tags VARCHAR(100))')

    def store_to_db(self, item):
        self.curr.execute('INSERT INTO quotes VALUES (%s, %s, %s)', (item['text'][0], item['author'][0], item['tags'][0]))
        self.conn.commit()

    def process_item(self, item, spider):
        print('Pipeline: Save item to MySQL database')
        self.store_to_db(item)
        return item


class MongoDBPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            host='localhost',
            port=27017,
            username='admin',
            password='password'
        )
        db = self.conn['myquotes']
        self.collection = db['quotes_db']

    def process_item(self, item, spider):
        print('Pipeline: Save item to MongoDB')
        document = {"author": item['author'][0], "text": item['text'][0], "tags": item['tags'][0]}
        self.collection.insert_one(document)
        return item
