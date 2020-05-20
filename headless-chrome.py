from selenium import webdriver              # Selenium play a vital role to control browsers with python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')      # This line is responsible for disabling the gpu 
driver = webdriver.Chrome(chrome_options=options)
