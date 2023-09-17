
import openpyxl 
from selenium import webdriver
import re
from openpyxl.styles import PatternFill
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting import Rule
from openpyxl.utils import get_column_letter
import time
from selenium.webdriver.common.by import By
import requests
import json
import os

# 创建Edge浏览器的驱动程序对象
driver = webdriver.Edge()
# 打开登录页面
driver.get('https://jw.jxyy.edu.cn:9002/jwglxt/xtgl/login_slogin.html')
# 执行登录操作，输入用户名和密码
username_input = driver.find_element(By.ID, "yhm")
password_input = driver.find_element(By.ID, "mm")
username_input.send_keys("用户名")
password_input.send_keys('xs123456')

# 点击登录按钮
login_button = driver.find_element(By.ID, "dl")
login_button.click()

# 等待登录完成和加载Cookie
driver.implicitly_wait(10)

time.sleep(3)
# 获取所有的Cookie信息
cookies = driver.get_cookies()

# 关闭浏览器
driver.quit()

aa=cookies[0]
cok=f'{aa["name"]}={aa["value"]}'
res=requests.post(
    url=f"http://111.75.254.215:9002/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N2151&su={user}",
    headers={
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Length":"28",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie":cok,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54"
    },
    data={
        "xnm": "2022",
        "xqm": "3",
        "kzlx": "ck",
    }
).json()
r=res["kbList"]