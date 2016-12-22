# -*- coding:utf-8 -*-

import MySQLdb
#from getmovieurl.items import GetmovieurlItem


class CreateDB():
    def __init__(self):
        self.host = "139.196.29.97"
        self.conn = MySQLdb.connect(self.host, user='root', passwd='TRzjy123', port=3306, charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def create_database(self):
        create_db_sql = 'CREATE DATABASE movie DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'
        self.cur.execute(create_db_sql)

    def create_table(self):
        self.conn.select_db('movie')
        self.cur.execute("create table market_info( market_name varchar(100), market_title varchar(100), \
                              market_time varchar(100), market_url varchar(100))")


class DBOperation():
    def __init__(self):
        self.conn = MySQLdb.connect(host="139.196.29.97", db='movie', user='root', passwd='TRzjy123', port=3306, charset='utf8', use_unicode=True)
        self.cur = self.conn.cursor()

    def insert_data(self, value):
        try:
            sql = "insert into \
                                  market_info(market_name,market_title,market_time, market_url) \
                                  values(%s,%s, %s, %s)"
            param = (value['market_name'], value['market_title'], value['market_time'], value['market_url'])
            self.cur.execute(sql, param)

        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def update_data(self, value):
        try:
            sql = "UPDATE market_info SET movie_url = '%s',movie_picurl = '%s' WHERE movie_name = '%s'" % (value['movie_url'], value['movie_picurl'], value['movie_name'])
            self.cur.execute(sql)

        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def select_data(self):
        try:
            max_sql = "SELECT max(movie_id) FROM market_info WHERE movie_url !=''"
            self.cur.execute(max_sql)
            number = self.cur.fetchall()
            print number
            if number[0][0]:
                print 'not none'
                sql = "SELECT movie_name FROM market_info WHERE movie_id > %s" % number[0][0]
            else:
                print 'none'
                sql = "SELECT movie_name FROM market_info"
            self.cur.execute(sql)
            results = self.cur.fetchall()
            return results
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def select_col(self):
        try:
            sel_col_sql = "SELECT movie_name,movie_url FROM market_info"
            self.cur.execute(sel_col_sql)
            sel_col_results = self.cur.fetchall()
            return sel_col_results

        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def delete_col(self, value):
        try:
            del_col_sql = "DELETE FROM market_info WHERE movie_name = '%s'" % value['movie_name']
          #  del_col_sql = "DELETE FROM old_movies WHERE movie_name = 'yy'"
        #    print del_col_sql
            self.cur.execute(del_col_sql)
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def delete_all(self):
        try:
            delete_all_sql = "truncate table market_info"
            self.cur.execute(delete_all_sql)
        except MySQLdb.Error, e:
            print "Mysql Error %d : %s" % (e.args[0], e.args[1])

    def dis_conn(self):
            self.conn.commit()
            self.cur.close()
            self.conn.close()


if __name__ == '__main__':
    value = {"movie_name": "神奇动物在哪里",
             "movie_rate":"8.9",
             "movie_director":"大卫·叶茨",
             "movie_writer":"J·K·罗琳",
             "movie_roles":"埃迪·雷德梅恩   凯瑟琳·沃特斯顿   丹·福勒   艾莉森·萨多尔   科林·法瑞",
             "movie_language":"英语",
             "movie_date":"2016-11-30",
             "movie_long":"133分钟",
             "movie_description":"zhaojiayu",
             "movie_picurl": u'https://img5.doubanio.com/view/photo/photo/public/p2390153126.jpg',
             "movie_url": u'http://www.cmdyhd.com/play/19799-1-0.html'}
  #  print value

#  创建表格
#    obj = CreateDB()
#    obj.create_table()

#  对数据库进行操作
    op_obj = DBOperation()
    op_obj.delete_all()

