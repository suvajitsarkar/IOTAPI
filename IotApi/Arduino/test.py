import MySQLdb

def mysqlconnect():
    try:
        db_connection = MySQLdb.connect("localhost","pi","openhabiann","SmartLab")
    except:
        print("can not connect to database")
        return 0

    print("Connected")
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT CURDATE();")
    m = cursor.fetchone()
    print("today date is ",m[0])
    db_connection.close()

mysqlconnect()
