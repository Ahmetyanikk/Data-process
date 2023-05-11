import requests
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

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)
df = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\futbolBot\akim-korumali-priz.xlsx')
df['Görsel1'] = pd.Series(dtype='string')
df['Görsel2'] = pd.Series(dtype='string')
df['Görsel3'] = pd.Series(dtype='string')
df['Görsel4'] = pd.Series(dtype='string')
df['Görsel5'] = pd.Series(dtype='string')

writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
for j in range(0,len(df['Ürün Adı'])):
    print(j)
    url = df.at[j,'urun_link']
    filename = df.at[j,'Ürün Adı']

    if url.split("//")[1][0] == 'c':
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
    elif url.split("//")[1][4] == 't':
        driver.get(url)
        time.sleep(10)
        asd = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        asd.click()
        for i in range(0, 5):
            try:
                x = driver.find_element(By.XPATH,
                                        "/html/body/div/div[5]/main/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div[" + str(
                                            i + 1) + "]/img")
                action.move_to_element(x).perform()
                asd = driver.find_element(By.XPATH,
                                          "/html/body/div/div[5]/main/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div/div/img")
                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)

    elif url.split("//")[1][4] == 'h' and url.split("//")[1][5] == 'e':
        driver.get(url)
        time.sleep(10)
        asd = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        asd.click()
        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 5):
            try:
                asd = driver.find_element(By.XPATH,
                                          "/html/body/div[2]/main/div[3]/section[1]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div/div[" + str(
                                              i + 1) + "]/a/picture/img")

                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)


    elif url.split("//")[1][4] == 'm':
        driver.get(url)

        time.sleep(10)
        asd = driver.find_element(By.XPATH, '/html/body/sm-root/div/fe-product-cookie-indicator/div/div/button[2]')
        asd.click()
        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 5):
            try:
                asd = driver.find_element(By.XPATH,
                                          "/html/body/sm-root/div/main/sm-product/article/sm-product-detail-page/div[1]/div[2]/sm-product-images/div/div[1]/swiper/div/div[" + str(
                                              i + 1) + "]/img")

                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)


    elif url.split("//")[1][4] == 'a':

        driver.get(url)

        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 1):
            try:
                asd = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/a/img")

                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)

    elif url.split("//")[1][4] == 'h' and url.split("//")[1][5] == 'a':

        driver.get(url)

        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 1):
            try:
                asd = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/a")

                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("href")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)


    elif url.split("//")[1][4] == 'a':

        driver.get(url)

        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 1):
            try:
                asd = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/a/img")

                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)

    elif url.split("//")[1][4] == 'n':

        driver.get(url)

        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 1):
            try:
                asd = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/a/img")

                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)

    elif url.split("//")[1][4] == 'c' and url.split("//")[1][5] == 'a':
        driver.get(url)
        time.sleep(10)

        driver.execute_script("window.scrollBy(0, 1000);")
        for i in range(0, 5):
            try:
                asd = driver.find_element(By.XPATH,
                                          "/html/body/main/div[4]/div[2]/div[1]/div/div/div[1]/div[1]/div/div[" + str(
                                              i + 1) + "]/div/div/span/img")


                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                print("bitti")
                break
            src = asd.get_attribute("src")
            print(src)
            response = requests.get(src)
            with open(filename + str(i + 1) + ".jpg", "wb") as f:
                f.write(response.content)

    elif url.split("//")[1][4] == 'e':
        driver.get(url)

        asd = driver.find_element(By.XPATH, '//*[@id="cookie_agree"]')
        asd.click()
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 1000);")

        for i in range(0, 5):
            try:
                asd = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div/div[4]/div[1]/div[2]/div[1]/div/div[1]/ul/li[" + str(
                                              i + 1) + "]/a/img")




                print(i)
            except selenium.common.exceptions.NoSuchElementException:
                asd = driver.find_element(By.XPATH,
                                          "/html/body/div[1]/div/div[4]/div[1]/div[2]/div[1]/div/div[1]/ul/li/a/img")
                print("bitti")
                if i>0:
                    break
            src = asd.get_attribute("src")
            src=src.replace("/s_", "/b_")
            print(src)
            df.at[j, 'Görsel'+str(i+1)]=src
        driver.quit()
        driver = webdriver.Chrome()

df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.close()

