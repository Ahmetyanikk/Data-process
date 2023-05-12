import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

#FUNCTIONS
def request_n_soup_special_for_epey(link,header):
    pageSource = requests.get(link, headers=header).content
    soup = BeautifulSoup(pageSource,"html.parser")
    return soup

def epey(link):
    soup = request_n_soup_special_for_epey(link,headers)
    photos = soup.find("ul",{"class":"galerik"}).find_all("img")
    for m in photos:
        divide_img = m['src'].split("/")
        divide_img[-1] = "b" + divide_img[-1][1:]
        img = "/".join(divide_img)
        print(img)
 
#https://www.ugur.com.tr/
def ugurDerinDondurucu(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find_all("img",{"class":"image-att"})
    for i in photos[:5]:
        print(i["data-lazy"])
#----------------------------------------------------

#https://www.karaca.com/
def karaca(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find_all("a",{"data-fslightbox":"gallery-web"})
    for i in photos[:5]:
        print(i["href"])
#----------------------------------------------------

#https://www.cimri.com/
def cimri(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("ul",{"class":"s1wxq1uo-1 hnSmng"}).find_all("li",{"class":"s1wxq1uo-2 iVTokt"})
    for index, i in enumerate(photos[:5]):
        img = i.find("img",{"class":"s51lp5-0 iRZUoF"})
        if(index == 0):
            print(img['src'].replace("240x240","1000x1000"))
        else:
            print(img['data-src'].replace("240x240","1000x1000"))
#----------------------------------------------------

#https://www.pazarama.com/
def pazarama(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("div",{"class":"swiper-wrapper"}).find_all("img",{"class":"object-contain w-full h-full"})
    for i in photos[:5]:
        print(i["data-src"].replace("150/150","600/600"))
#----------------------------------------------------

#https://www.vestel.com/
def vestel(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("ul",{"class":"image-slider-thumbs product"}).find_all("img",{"class":"hidden-m lazy"})
    for i in photos[:5]:
        print(i["data-lazy"])
#----------------------------------------------------

#https://www.singer.com/
def singer(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("div",{"class":"img-cont multi"}).find_all("img")
    for i in photos[:5]:
        print(i["src"])
#----------------------------------------------------

#www.siemens-home.bsh-group.com
def siemens(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find_all("div",{"class":"a-image"})# #
    #print(photos)
    for i in photos[1:6]:
        tag = i.find("img")
        img = tag["src"].split("/")
        img[4] = "1200x675"
        img_modified = "/".join(img)
        print(img_modified)

#www.arcelik.com.tr
def arcelik(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("div",{"class":"swiper-wrapper"}).find_all("img")
    for i in photos[:5]:
        source = i['data-srcset'].split(", ")
        img = source[-1][0:-3]
        img_link = "https://www.arcelik.com.tr" + img
        print(img_link)
#----------------------------------------------------

#www.ciceksepeti.com
def ciceksepeti(link_par):
    scraper = WebScrappingDriver()
    try:
        scraper.scrap_data(link_par)
        soup = scraper.get_page_source_soup()
        photos1 = soup.find_all("div",{"class":"product__thumbs-item js-product__thumbs-item product__thumbs-item-json br-6 active"})
        photos = soup.find_all("div",{"class":"product__thumbs-item js-product__thumbs-item product__thumbs-item-json br-6"})
        photos.append(photos1[0])

        for i in photos[:5]:
            print(i.find("a")['data-href'])

        scraper.quit_driver()
    except:
        scraper.quit_driver()
#----------------------------------------------------

#https://www.amazon.com.tr/
def amazontr(link_par):
    scraper = WebScrappingDriver()
    try:     
        scraper.scrap_data(link_par)
        scraper.click_By_xpath('//*[@id="landingImage"]')
        time.sleep(1)
        soup = scraper.get_page_source_soup()
        small_soup = soup.find("div",{"id":"ivThumbs"})
        photos = small_soup.find_all("div",{"class":"ivThumb"})
        
        count_photos = len(photos)-1
        if(count_photos>5):
            count_photos = 5

        #İlk img
        img_tag = soup.find("div",{"id":"ivLargeImage"}).find("img")
        print(img_tag['src'])

        #Geri kalan imgler
        for i in range(1,count_photos):

            scraper.click_By_id("ivImage_"+str(i))
            time.sleep(1)
            soup = scraper.get_page_source_soup()
            img_tag = soup.find("div",{"id":"ivLargeImage"}).find("img")
            print(img_tag['src'])
        
        scraper.quit_driver()

    except:
        scraper.quit_driver()
#----------------------------------------------------

#www.hepsiburada.com
def hepsiburada(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("div",{"id":"productDetailsCarousel"}).find_all("picture")
    #ilk img
    print(photos[0].find("source")['srcset'].split(" ")[0])
    #kalan imgler
    for i in photos[1:5]:
        print(i.find("source")['data-srcset'].split(" ")[0])
#----------------------------------------------------
