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
df = pd.DataFrame({'Ürün id': [],
                   'Ürün ismi': [],
                   'Link':[]})
writer = pd.ExcelWriter('pazaramaTelefon'+'.xlsx', engine='openpyxl')

chrome_options = Options()
chrome_options.add_argument("--start-maximized")



row=0
for i in range (1,19):
    print(i)
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://www.pazarama.com/cep-telefonu-k-K03043?sayfa='+str(i)
    driver.get(url)
    time.sleep(20)
    asd=driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/header/div[1]/div[3]/div/ul/li[5]/a/span")


    for k in range(0,20):
        if i==1:
            x = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div["+str(k+1)+"]").text
            y= driver.find_element(By.XPATH, "/ html / body / div[1] / div / div / div[1] / div / div[2] / div / div[2] / div[2] / div["+str(k+1)+"] / div / a")
        else:
            x = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[" + str(k + 1) + "]").text
            y = driver.find_element(By.XPATH, "/ html / body / div[1] / div / div / div[1] / div / div[2] / div / div[2] / div[3] / div[" + str( k + 1) + "] / div / a")


        a=y.get_attribute("href").split("-p-")
        df.at[row,'Ürün id']=a[1]
        df.at[row,'Link']=y.get_attribute("href")
        single_row_string = " ".join(x.split("\n"))
        # print(single_row_string)  # "row1 row2"
        df.at[row, 'Ürün ismi'] =single_row_string
        row=row+1
    driver.quit()


df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()
