#https://www.ugur.com.tr/
def ugurDerinDondurucu(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find_all("img",{"class":"image-att"})
    for i in photos[:5]:
        print(i["data-lazy"])

#https://www.karaca.com/
def karaca(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find_all("a",{"data-fslightbox":"gallery-web"})
    for i in photos[:5]:
        print(i["href"])

#https://www.cimri.com/
def cimri(link_par):
    scraper = WebScrappingDriver()
    scraper.scrap_data(link_par)
    scraper.click_By_xpath('//*[@id="main_container"]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/ul/li[1]/img')
    soup = scraper.get_page_source_soup()
    scraper.quit_driver()

    photos = soup.find_all("div",{"class":"s75m7lh-0 qYSgN"})
    for i in photos[:5]:
        print(i.find("img")['src'])


#https://www.pazarama.com/
def pazarama(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("div",{"class":"swiper-wrapper"}).find_all("img",{"class":"object-contain w-full h-full"})
    for i in photos[:5]:
        print(i["data-src"].replace("150/150","600/600"))


#https://www.vestel.com/
def vestel(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("ul",{"class":"image-slider-thumbs product"}).find_all("img",{"class":"hidden-m lazy"})
    for i in photos[:5]:
        print(i["data-lazy"])

#https://www.singer.com/
def singer(link_par):
    soup = request_n_soup(link_par)
    photos = soup.find("div",{"class":"img-cont multi"}).find_all("img")
    for i in photos[:5]:
        print(i["src"])
