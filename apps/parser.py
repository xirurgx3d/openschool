# Приложение берёт джейсон с карточками Анки и заполняет их недостающими данными 
# Данная версия программы работает с 
#
#
#


import parserapp.settings as settings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Firefox(executable_path=settings.env["pathseleniumdriver"])
driver.get("http://www.wikipedoa.org")



# 