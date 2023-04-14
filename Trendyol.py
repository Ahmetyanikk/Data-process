import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pandas
from openpyxl import load_workbook
import pandas as pd

df = pd.DataFrame({
                   'Ürün ismi': [],
                   'Link':[]})

adi="Biberon"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.trendyol.com/sr?q=biberon&qt=biberon&st=biberon&os=1&sst=BEST_SELLER&pi=4'
driver.get(url)
time.sleep(15)


asd=driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
asd.click()
driver.execute_script("window.scrollBy(0, 3000);")
time.sleep(10)

writer = pd.ExcelWriter(adi+' Hepsiburada.xlsx', engine='openpyxl')
