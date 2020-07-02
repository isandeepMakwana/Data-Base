# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:13:32 2020

@author: shivang dargar
"""

import mysql
import mysql.connector
def dbconn():
    try:
        mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                password="sandeepmakwana@123",
                )
        if mydb.is_connected():
            print("connected successful")
    except Error as e:
        print("rause connceted",e)
    finally:
        if mydb.is_connected():
            mydb.close()
            print("connection closed")
dbconn()

