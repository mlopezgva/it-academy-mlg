import dateutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import configparser
import mysql.connector

cfgFp = open(r'C:\Users\formacio\Downloads\mlg\git_repo\SPRINT8\db.ini', mode='r')
iniFp = configparser.ConfigParser()
iniFp.read_file(cfgFp)
dbCfg = dict(iniFp.items('database'))

# exit()

db = mysql.connector.connect(
    host=dbCfg['host'],
    database=dbCfg['database'],
    user=dbCfg['user'],
    password=dbCfg['password']
)

tr_df   = pd.read_sql("SELECT * FROM `transaction`", db)

user_df = pd.read_sql("SELECT * FROM `user`", db)

co_df = pd.read_sql("SELECT * FROM company", db)

pr_df   = pd.read_sql("SELECT * FROM product", db)
prtr_df = pd.read_sql("SELECT * FROM product_transaction", db)

def age(birthdate):
    dob = pd.to_datetime(birthdate).date() if type(birthdate) is not str \
                  else dateutil.parser.parse(birthdate).date()
    hoy = dateutil.utils.today().date()
    ddiff = hoy - dob
    edad  = int(ddiff.days / 365.25)
    return edad

# Add age column to user dataframe
user_df["age"] = user_df['birthdate'].map(age)
