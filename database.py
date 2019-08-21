import sqlite3
import mysql.connector
# from mysql.connector import MySQLConnection


conn = sqlite3.connect('quotes.db')
curr = conn.cursor()
curr.execute('CREATE TABLE IF NOT EXISTS quotes(text text, author text, tags text)')
curr.execute('INSERT INTO quotes VALUES ("Any text", "Fritz Mueller", "any_tag")')
conn.commit()
conn.close()

# cnx = MySQLConnection(user='joe', database='test')
# conn = mysql.connector.connect(
#             host='localhost',
#             port='9002',
#             user='root',
#             password='example'
#         )
# curr = conn.cursor()
# curr.execute('CREATE DATABASE IF NOT EXISTS scrapy')
# curr.execute('USE scrapy')
# curr.execute('CREATE TABLE IF NOT EXISTS quotes (text text, author text, tags text)')
# conn.commit()
# conn.close()
