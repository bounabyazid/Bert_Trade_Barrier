#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 27 04:46:24 2020

@author: Yazid BOUNAB
"""

'https://www.datacamp.com/community/tutorials/mysql-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034349&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1005766&gclid=Cj0KCQjwwuD7BRDBARIsAK_5YhU5urXSQbjsR4qHRjkWvGXm3L9sZUJVfn18iPfZt8Kv9RqwKlqzvioaArI5EALw_wcB'

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "polo",
    passwd = "Polo12369*",
    database = "T_barrier"
)

cursor = db.cursor()

def Sections():
    query = "INSERT INTO Sections (Title) VALUES (%s)"
    
    values = ("Hafeez", "hafeez")
    
    values = [
            ("Peter", "peter"),
            ("Amy", "amy"),
            ("Michael", "michael"),
            ("Hennah", "hennah")
            ]
    cursor.execute(query, values)

    db.commit()


cursor.execute("SHOW TABLES")

Tables = cursor.fetchall()



print(Tables)
