# from flask import Flask,redirect,render_template,request
# import pypyodbc

# app = Flask(__name__)

# server = 'assign1server.database.windows.net'
# database = 'sqldb'
# username = 'saitheja'
# password = '9705004946S@i'
# driver= '{ODBC Driver 13 for SQL Server}'

# def disdata():
#     dbconn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
#     cursor = dbconn.cursor()
#     start = time.time()
   
#     success="SELECT * from [dbo.people] "
#     cursor.execute(success)
#     end = time.time()
#     exectime = end - start
#     return render_template('count.html', t=exectime)

# @app.route('/')
# def hello_world():
#   return disdata('index.html')

# if __name__ == '__main__':
#   app.run()
# import pyodbc 
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=assign1server.database.windows.net;'
#                       'Database=assignment1;'
#                       'Trusted_Connection=False;'
#                       'Encrypt=True;'
#                       'Integrated Security=False'
#                       )

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM database_name.dbo.people')

# for row in cursor:
#     print(row)




from flask import Flask,redirect,render_template,request
import textwrap
import pyodbc
import time


app = Flask(__name__)

driver = '{ODBC Driver 17 for SQL Server}'
server_name = 'assign1server'
database_name = 'assignment1'
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)
username = "saitheja"
password = "9705004946S@i"

def search(name=None):
    connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
))
    cnxx: pyodbc.Connection = pyodbc.connect(connection_string)
    crsr: pyodbc.Cursor = cnxx.cursor()
    start = time.time()
    select_sql = "SELECT Picture FROM dbo.people where Name = '"+name+"'";
    crsr.execute(select_sql)
    data = crsr.fetchone()
    rows = data[0]   

    print(crsr.fetchall())
    end = time.time()
    cnxx.close()
    exectime = end - start
    return render_template('count.html', t=rows)

@app.route('/img')
def display():
    name = request.args.get('name')
    return search(name)

@app.route('/')
def hello_world():
    return render_template('index.html')



if __name__ == '__main__':
  app.run()