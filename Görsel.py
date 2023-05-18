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
import glob
import requests
from bs4 import BeautifulSoup

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
def request_n_soup_special_for_epey(link,header):
    pageSource = requests.get(link, headers=header).content
    soup = BeautifulSoup(pageSource,"html.parser")
    return soup


action = ActionChains(driver)
inputpath = r"C:\\Users\\Ahmet\\PycharmProjects\\futbolBot\\venv\\inputexcel\\"
outputpath = r"C:\\Users\\Ahmet\\PycharmProjects\\futbolBot\\venv\\outputexcel\\"
excelpath = glob.glob(inputpath+"*.xlsx")


writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
for excel in excelpath:
    print(excel)

    filename = excel.split('\\')[-1][:-5]

    df = pd.read_excel(excel)
    df['Görsel1'] = pd.Series(dtype='string')
    df['Görsel2'] = pd.Series(dtype='string')
    df['Görsel3'] = pd.Series(dtype='string')
    df['Görsel4'] = pd.Series(dtype='string')
    df['Görsel5'] = pd.Series(dtype='string')
    for j in range(0, len(df['Tittle'])):
        print(j)
        url = df.at[j, 'Link']
        filename = df.at[j, 'Tittle']
        mainUrl = url.split(".")[1]

        if url.split("//")[1][0] == 'c':
            response = requests.get(url)
            with open(filename, "wb") as f:
                f.write(response.content)
        elif mainUrl == 'trendyol':
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

        elif mainUrl == 'hepsiburada':
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


        elif mainUrl == 'migros':
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


        elif mainUrl == 'akakce':

            driver.get(url)

            time.sleep(5)

            
            for i in range(0, 5):
                try:
                    asd = driver.find_element(By.XPATH,
                                              "/html/body/main/div[1]/div/div[2]/div[2]/a["+str(i+1)+"]/img")

                    print(i)
                except selenium.common.exceptions.NoSuchElementException:
                    asd = driver.find_element(By.XPATH,
                                              "/html/body/main/div[1]/div/div[2]/div[2]/a/img")
                    print("bitti")
                    if i > 0:
                        break
                src = asd.get_attribute("src")
                print(src)
                response = requests.get(src)
            df.at[j, 'Görsel' + str(i + 1)] = src

        elif mainUrl == 'happycenter':

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



        elif mainUrl == 'n11':

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

        elif mainUrl == 'carrefoursa':
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

        elif mainUrl == 'epey':
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
                    if i > 0:
                        break
                src = asd.get_attribute("src")
                src = src.replace("/s_", "/b_")
                print(src)
                df.at[j, 'Görsel' + str(i + 1)] = src
            driver.quit()
            driver = webdriver.Chrome(options=chrome_options)

    df.to_excel(outputpath + f'{filename}' + ".xlsx", index=False)



