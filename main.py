from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
#options.add_argument("--headless")
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

browser = webdriver.Firefox(executable_path=r'C:\Users\dell\Desktop\ms\geckodriver.exe', options=options)
browser.get('http://selenium.dev/')
