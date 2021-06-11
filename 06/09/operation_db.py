import pymysql
from .conf import conf
import os

class opration_db(object):
    print(os.getcwd())
    def insert_table(self):

        c = conf.db_conf()
        db = pymysql.connect(
            host = c.host,
            port = c.port,
            db = c.db,
            user = c.user,
            passwd = c.passwd,
            charset = 'utf8'
        )
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS USER")
        sql = "CREATE TABLE USER(id int, name varchar(100),address varchar(100), phone int, sex varchar(100))"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()


if __name__ == "__main__" :
    od = opration_db()
    od.insert_table()