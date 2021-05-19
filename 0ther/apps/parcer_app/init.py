import os
from dotenv import load_dotenv
load_dotenv()

DRIVER_PATH = os.getenv('DRIVER_PATH')


class Driver():

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time 
    login = webdriver.Firefox(executable_path=r'/home/user/Apps/GeckoDriver/geckodriver')