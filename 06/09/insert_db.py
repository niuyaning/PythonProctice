import pymysql
from .config import conf


class opration_db():

    def insert_db(self):

        db = pymysql.connect(
            host=conf.host,
            user=conf.user,
            port=conf.port,
            passwd=conf.passwd,
            db="db",
            charset='utf8')

        cursor = db.cursor()
        sql = "INSERT INTO USER VALUES (1,'张三','北京市昌平区',150,'男')"
        try:
            result = cursor.execute(sql)
            db.commit()
            print(result)
        except:
            db.rollback()


if __name__ == "__main__":
    od = opration_db()
    od.select_db()
