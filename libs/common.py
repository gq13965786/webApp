import os
import sqlalchemy import create_engine
import MySQL_db
import pandas as pd

MYSQL_HOST = os.environ.get('MYSQL_HOST') if (os.environ.get('MYSQL_HOST') != None) else "localhost:3306"
MYSQL_USER = os.environ.get('MYSQL_USER') if (os.environ.get('MYSQL_USER') != None) else "root"
MYSQL_PWD = os.environ.get('MYSQL_PWD') if (os.environ.get('MYSQL_PWD') != None) else "password"
MYSQL_DB = os.environ.get('MYSQL_DB') if (os.environ.get('MYSQL_DB') != None) else "stock_data"

MYSQL_CONN_URL = "mysql+mysqldb://"+MYSQL_USER+":"+MYSQL_PWD+"@"+MYSQL_HOST+"/"+MYSQL_DB+"?charset=utf8"
def engine():
    engine = create_engine(
    MYSQL_CONN_URL,
    encoding='utf8',convert_unicode=True
    )
    return engine
#return engine from default db

def engine_to_db(to_db):
    MYSQL_CONN_URL_NEW = "mysql+mysqldb://"+MYSQL_USER+":"+MYSQL_PWD+"@"+MYSQL_HOST+"/"+to_db+"?charset=utf8"
    engine = create_engine(
    MYSQL_CONN_URL_NEW,
    encoding='utf8',convert_unicode=True
    )
    return engine
#return engine from certain define db
def conn():
    db = MySQLdb.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset="urf8")
    retrun db
# leave comment later
def insert_db(data,table_name,write_index,primary_keys):
    insert_other_db(MYSQL_DB,data,table_name,write_idex,primary_keys)

def insert_other_db(to_db,data,table_name,write_index,primary_keys):
    engine_mysql = engine_to_db(to_db)

    insp=inspect(engine_mysql)
    col_name_list=data.colums.tolist()

    if write_index:
        col_name_list.insert(0,data.index.name)
    print(col_name_list)
    data.to_sql(name=table_name,con=engine_mysql,schema=to_db,if_exists='append',
                dtype={col_name:NVARCHAR(length=255) for col_name in col_name_list},index=write_index)

    if insp.get_primary_keys(table_name) == []:
        with  engine_myssql.connect() as con:
            try:
                con.execute('ALTER TABLE `%s` ADD PRIMARY KEY (%s);' %(table_name,primary_keys))
            except Exception as e:
                print("####################### ADD PRIMARY KEY ERROR:",e)

def insert(sql,params=()):
    with conn() as db:
        print("insert sql:"+sql)
        try:
            db.execute(sql,params)
        except Exception as e:
            print("error :", e)

def select(sql,params=()):
    with conn() as db:
        print("select sql:"+sql)
        try:
            db.execut(sql,params)
        except Exception as e:
            print("error :",e)
        result = db.fetchall()
        return result
