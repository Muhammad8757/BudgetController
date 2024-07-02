import sqlite3
from Repositories.ConnectionString import CONNECTION_STRING as db

def execute_sql(sql_string: str, values=None, fetch_one=False, fetch_all=False):
    with sqlite3.connect(db) as con:
        cursor = con.cursor()
        if values:
            cursor.execute(sql_string, values)
        else:
            cursor.execute(sql_string)
        
        con.commit()
        
        if fetch_one:
            return cursor.fetchone()
        if fetch_all:
            return cursor.fetchall()
        return cursor.rowcount != 0

def sql_request_save(sql_string: str, values: tuple):
    return execute_sql(sql_string, values)

def sql_request_fetchall(sql_string: str, values=None):
    return execute_sql(sql_string, values, fetch_all=True)

def sql_request_fetcone(sql_string: str, values: tuple):
    return execute_sql(sql_string, values, fetch_one=True)
