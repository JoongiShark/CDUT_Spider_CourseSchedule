import time
import hashlib

from hashlib import md5
from scrapy import Request, FormRequest
from scrapy.spiders import Spider
from scrapy.selector import Selector

from dbspider.items import Course


class CDUT_Class_Schedule(Spider):
    name = 'getCookies'
    allowed_domains = ['202.115.133.173:805']
    login_url = 'http://202.115.133.173:805/Login.html'

    def start_requests(self):
        timestamp = int(time.time() * 1000)
        formdata = {
            'userName': '账号',
            'pwd': '密码',
        }
        for classid in range(1, 5):
            for stuid in range(1, 31):
                stu_no = f'201608030%d%02d' % (classid, stuid)
                print(stu_no)
                cou_url = f'http://202.115.133.173:805/Classroom/ProductionSchedule/StuProductionSchedule.aspx?termid=201802&stuID={stu_no}'
                formdata['cou_url'] = cou_url
                print(formdata)
                yield Request(self.login_url, callback=self.parse_login, meta=formdata, dont_filter=True)

    def parse_login(self, response):
        print('===========================================================')
        courses_data = response.css('.fontcss')
        courses = []
        for c in courses_data:
            if c.xpath('./@colspan'):
                time = int(c.xpath('./@colspan').extract_first())
                for i in range(time):
                    courses.append(c.xpath('./text()').extract_first())
            else:
                courses.append(c.xpath('./text()').extract_first())
        week_day_course_list = [[[courses[j * 12 * 7 + l * 12 + i] for i in range(12)] for l in range(7)] for j in range(20)]
        item = Course()
        item['course_detail'] = str(week_day_course_list)
        item['stu_id'] = response.url[-12:]
        yield item

