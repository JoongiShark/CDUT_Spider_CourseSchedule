# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql


class DbspiderPipeline(object):
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            )

    def open_spider(self, spider):
        # 获取数据库连接
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        # 释放数据库连接
        self.db.close()

    def process_item(self, item, spider):
        if item.collection == 'course':
            sql = 'insert into stu_course (stu_id, course_detail) values (%s, %s)'
            self.cursor.execute(sql, (item['stu_id'], item['course_detail']))
            self.db.commit()

        return item



