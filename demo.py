# -*- coding:utf-8 -*-


import os
import ddt, time, HTMLTestRunner
import unittest
from htmloutput.htmloutput import HtmlOutput
from nose import run
from selenium import webdriver


from base import read_excel

# test_data1 = [{"username": "zhangsan"},
#              {"username": "lisi"},
#              ]

# test_data1 = (['liuzunrui', '12312421'],
#               ['fasgaeg', '12432535'])

data = read_excel.ExcelUtil('data/data.xlsx', '1')
test_data1 = data.get_data()
print test_data1


@ddt.ddt
class testBaidu(unittest.TestCase):

    def setUp(self):
        self.drvier = webdriver.Chrome('/usr/local/bin/chromedriver')
        driver = self.drvier
        driver.get('http://mada.zhengyitech.com/pages/login.html')
        driver.implicitly_wait(10)

    # @ddt.data(*test_data1)
    # @ddt.unpack
    def baidu(self, provience, code):
        driver = self.drvier
        driver.find_element_by_css_selector('#login-form > div:nth-child(1) > input').click()
        driver.find_element_by_css_selector('#login-form > div:nth-child(1) > input').send_keys(provience)
        time.sleep(1)
        driver.find_element_by_css_selector('#first-password').clear()
        driver.find_element_by_css_selector('#first-password').send_keys(code)
        time.sleep(1)
        self.drvier.get_screenshot_as_file(provience + '.png')

    @ddt.data(*test_data1)
    def test_baidu(self, data):
        self.baidu(data['provience'], int(data['code']))

    def tearDown(self):
        self.drvier.quit()


