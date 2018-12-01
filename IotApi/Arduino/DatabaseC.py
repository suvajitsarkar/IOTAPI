import MySQLdb
def dbEntry(sql):
    db = MySQLdb.connect("localhost","pi","openhabiann","SmartLab")
    cursor= db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print e
        db.rollback()
    db.close()
