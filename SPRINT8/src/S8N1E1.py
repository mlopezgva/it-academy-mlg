import dateutil
import pandas as pd
import numpy as np
import configparser
import mysql.connector
import pandas as pd

LF="\n"

def is_defined(varname):
    return varname in globals()

# Conectar con la base de datos. Datos de la conexión en db.ini
# Devuelve la variable `db` para poder usarla en otros ambientes
# (al definirla en el módulo, no es visible fuera, así que la devuelve
# para que esté disponible para quien ha pedido la conexión)
def db_connect():
    try:
        cfgFp = open(r'C:\Users\formacio\Downloads\mlg\git_repo\SPRINT8\db.ini', mode='r')
        print (cfgFp)
        iniFp = configparser.ConfigParser()
        iniFp.read_file(cfgFp)
        dbCfg = dict(iniFp.items('database'))

        # print(dbCfg, dbCfg['host'])
        # exit()

        if not is_defined('db') or not db.is_connected():
            db = mysql.connector.connect(
                host=dbCfg['host'],
                database=dbCfg['database'],
                user=dbCfg['user'],
                password=dbCfg['password']
            )
            print("Conectado!")

        return db

    except Exception as e:
        exit("Error:", e)

def is_dataFrame(varname):
    return is_defined(varname) \
        and type(globals().get(varname)) is pd.core.frame.DataFrame

def load_tables():
    global tr_df, user_df, co_df, pr_df, prtr_df
    try:
        if not is_dataFrame('tr_df'):
            tr_df   = pd.read_sql("SELECT * FROM `transaction`", db)
            print("Tabla 'transaction' cargada correctamente")

        if not is_dataFrame('user_df'):
            user_df = pd.read_sql("SELECT * FROM `user`", db)
            print("Tabla 'user' cargada correctamente")

        if not is_dataFrame('co_df'):
            co_df = pd.read_sql("SELECT * FROM company", db)
            print("Tabla 'company' cargada correctamente")

        if not is_dataFrame('prtr_df'):
            pr_df   = pd.read_sql("SELECT * FROM product", db)
            prtr_df = pd.read_sql("SELECT * FROM product_transaction", db)
            print("Tablas 'product' y 'product_transaction' cargadas correctamente")

        else:
            return

    except:
        print("Error leyendo la DB...")

db = db_connect()

if not is_dataFrame('user_df'):
    load_tables()

def age(birthdate):
    dob = pd.to_datetime(birthdate).date() if type(birthdate) is not str \
                  else dateutil.parser.parse(birthdate).date()
    hoy = dateutil.utils.today().date()
    ddiff = hoy - dob
    edad  = int(ddiff.days / 365.25)
    # print(edad, "años")
    return edad

# Add age column to user dataframe
user_df["age"] = user_df['birthdate'].map(age)

# print(user_df)

age_distrib_graph = user_df.groupby('age')['age'] \
        .count() \
        .plot.bar(
            x='age',
            figsize=(10,5),
            title="Age distribution",
            ylabel="# of Users",
            xlabel="Age"
        )

