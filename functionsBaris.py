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
    soup = request_n_soup(link_par)
    photos = soup.find("ul",{"class":"s1wxq1uo-1 hnSmng"}).find_all("li",{"class":"s1wxq1uo-2 iVTokt"})
    for index, i in enumerate(photos[:5]):
        img = i.find("img",{"class":"s51lp5-0 iRZUoF"})
        if(index == 0):
            print(img['src'].replace("240x240","1000x1000"))
        else:
            print(img['data-src'].replace("240x240","1000x1000"))

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
