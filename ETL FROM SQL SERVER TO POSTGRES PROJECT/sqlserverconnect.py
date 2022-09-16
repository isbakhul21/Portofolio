#import needed libraries
import pyodbc
import os
import psycopg2


#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#sql db details
driver = "{SQL Server Native Client 11.0}"
server = "LAPTOP-RR6QESQB"
database = "AdventureWorksDW2019;"

#Connection SQL SERVER 2019
sqls_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS' + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
sqls_cursor = sqls_conn.cursor()

#connection POstgres
psql_conn = psycopg2.connect( host="localhost", user=uid, password=pwd, database="DWH", port=5432)
psql_cursor = psql_conn.cursor()

# execute query di SQL Server
sql_get_column_name =   """
        SELECT c.COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS c
        WHERE TABLE_NAME = 'DimCustomer' 
        AND COLUMN_NAME IN ('FirstName', 'LastName');
        """
sqls_get_data = """
                SELECT TOP 10 FirstName, LastName 
                FROM AdventureWorksDW2019.dbo.DimCustomer;
                """
sql_postgres =  """
                INSERT INTO customers (FirstName, LastName) VALUES (%s, %s)
                """

#Execute SQL server to get column name
sqls_cursor.execute(sql_get_column_name)
sqls_column = sqls_cursor.fetchall()
#Merubah Data Loop ke Data List
column_name = [c[0] for c in sqls_column]

#Excecute SQL Server to get data from column
sqls_cursor.execute(sqls_get_data)
column_data = sqls_cursor.fetchall()

#Load Ke Postgres
psql_cursor.execute(f"CREATE TABLE Customers ({column_name[0]} character(50), {column_name[1]} character(50))")
psql_cursor.executemany(sql_postgres, column_data)
psql_conn.commit()

print("DATA SUDAH MASUK KE POSTGRES")


#Important To CLOSE ALL CURSOR AND CONNECTION

sqls_cursor.close()
psql_cursor.close()

sqls_conn.close()
psql_conn.close()

