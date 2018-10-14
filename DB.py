import pymysql
import time


class DB:

    # 数据库查询
    def get_dbdata(self, sql, db):
        conn = pymysql.connect(host='192.168.0.3', port=3306, user='digi', passwd='digi123456', db=db,
                               charset="utf8")
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
        cur.close()
        conn.close()

    #查询用户ID
    def get_userid(self,user):
        id = DB().get_dbdata("select user_id from user where  phone={0};".format(user),'coin')
        return int(id[0][0])
