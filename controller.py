# -*- coding:utf-8 -*-
# Author:Jake Jia
import mysql.connector
config = {
    'user': 'root',
    'password':  '123456',
}
conn = mysql.connector.connect(**config)
curs = conn.cursor()

