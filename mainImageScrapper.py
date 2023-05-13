import functionsBaris
import os
import pandas as pd

#Okunacak Excellerin bulunduğu dosya
arr = os.listdir('C:/Users/baris/Masaüstü/FotografCekme/PAZARAMA BİTENLER')#okunacak excel dataları(pazarama excelleri) başlık adı: "Ürün Sayfası"

#columns
columns = ["Görsel1","Görsel2","Görsel3","Görsel4","Görsel5"]

#Excel dosyasına, Marka kolonunun sağına olacak şekilde 5 tane Görsel kolonu ekle
def add_image_columns(pandas_par):
    try:
        title_index = pandas_par.columns.get_loc("Tittle")
        pandas_par.insert(title_index+1, "Varyant Id", None)
        pandas_par.insert(title_index+2, "Varyant Adi", None)
        pandas_par.insert(title_index+2, "Ürün Açıklaması", None)
    except:
        pass
    
    try:
        url_column_index = pandas_par.columns.get_loc("Marka")
    except:
        url_column_index = pandas_par.columns.get_loc("Ürün Sayfası")

    pandas_par.insert(url_column_index+1, columns[0], None) #Görsel1 kolonu eklendi
    pandas_par.insert(url_column_index+2, columns[1], None)
    pandas_par.insert(url_column_index+3, columns[2], None)
    pandas_par.insert(url_column_index+4, columns[3], None)
    pandas_par.insert(url_column_index+5, columns[4], None)




for i in arr[0:1]: #Toplu okunacak Excel dosyaları #"for i in arr[0:1]" bunu  multiFiles ile değiştir
    input_categories = pd.read_excel("C:/Users/baris/Masaüstü/FotografCekme/PAZARAMA BİTENLER/"+i)
    input_categories = input_categories.reset_index(drop=True) # make sure indexes pair with number of rows

    add_image_columns(input_categories) #Excelleri görsel kolonlarını ekle

    index_of_first_img_column = input_categories.columns.get_loc("Görsel1")

    for index, row in input_categories.iterrows():
        urun_link = row["Ürün Sayfası"]

        if(type(urun_link) == float):
            urun_link = "/////////"

        #EKLENECEK KISIM!!!!!!!!!!!!!
        if(urun_link.split("/")[2] == "www.pazarama.com"):
            img_links = functionsBaris.pazarama(urun_link)
            for index_img, j in enumerate(img_links):
                input_categories.at[index, input_categories.columns[index_of_first_img_column + index_img]] = j
        #-----------------------------------------------

        
        #if elif diye bütün siteler aşşağı inecek

    
    #bazı kolonları kaldır
    try:
        input_categories.drop('Ürün Sayfası', inplace=True, axis=1)
    except:
        pass
    try:
        input_categories.drop('Url', inplace=True, axis=1)
    except:
        pass
    try:
        input_categories.drop('Kaynak', inplace=True, axis=1)
    except:
        pass

    excele_isim = i.replace(".xlsx","").replace("/","_").lower()
    #excel dosyası değişmeden bu excel dosyası kaydedilecek
    with pd.ExcelWriter("C:/Users/baris/Masaüstü/FotografCekme/PAZARAMA BİTENLER output/"+i) as writer:
        input_categories.to_excel(writer,sheet_name=excele_isim, index=False)

choice = input('Press q to Quit')
if choice == "q":
    # break or return or..
    import sys
    sys.exit(0)
