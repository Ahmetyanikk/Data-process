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
df = pd.DataFrame({'Kategori': [],
                   'Ürün ismi': [],
                   'Link':[]})

writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')



chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.kikomilano.com.tr/fondoten/?page=50'
driver.get(url)
time.sleep(10)
asd=driver.find_elements(By.CLASS_NAME,"js-product-wrapper")

for i in range(0,len(asd)):
    x = driver.find_elements(By.CLASS_NAME, "product-name")[i].text
    df.at[i,'Kategori']='Fondöten'
    df.at[i,'Link']=asd[i].get_attribute("href")
    single_row_string = " ".join(x.split("\n"))
   # print(single_row_string)  # "row1 row2"
    df.at[i, 'Ürün ismi'] =single_row_string

df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()

