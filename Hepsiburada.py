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
url = 'https://www.hepsiburada.com/biberonlar-c-301172?siralama=coksatan'
driver.get(url)
time.sleep(15)


asd=driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
asd.click()
driver.execute_script("window.scrollBy(0, 3000);")
time.sleep(10)

writer = pd.ExcelWriter(adi+' Hepsiburada.xlsx', engine='openpyxl')

#/html/body/div[3]/main/div[2]/div/div[7]/div/div[2]/div/div[3]/div/div/div/div/div/div/ul[1]/li[14]/div/a/div[2]/h3
#for i in range(0,12):

  #  x = driver.find_element(By.XPATH,
  #                          "/html/body/div[3]/main/div[2]/div/div[7]/div/div[2]/div/div[3]/div/div/div/div/div/div/ul/li["+str(i+1)+"]/div/a/div[2]/h3")
  #  print(x.text)
print("asd")
#for i in range(13,200):
   # x = driver.find_element(By.XPATH,
   #                         "/html/body/div[3]/main/div[2]/div/div[7]/div/div[2]/div/div[3]/div/div/div/div/div/div/ul["+str(i//13)+"]/li[" + str(
   #                             i + 1) + "]/div/a/div[2]/h3")
   # print(x.text)


for i in range(0,200):
    if i%12==0 and i!=12 and i!=0:
        print("asd")
        driver.get("https://www.hepsiburada.com/biberonlar-c-301172?siralama=coksatan&sayfa="+str(i//12))
        driver.refresh()
        time.sleep(30)


    print(i)
    x = driver.find_elements(By.CLASS_NAME,'productListContent-zAP0Y5msy8OHn5z7T_K_')[i].text
    single_row_string =x.split("\n")
    df.at[i, 'Link'] = x[i].get_attribute("href")
    df.at[i, 'Ürün ismi'] = single_row_string[0]
    print(single_row_string[0])

df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()
