import pandas as pd
import math
import win32com.client as win32

dfHam = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\untitled6\Amerikan Servis.xlsx')
dfSayfa3=pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\untitled6\Amerikan Servis.xlsx','Sayfa3')


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
url="https://www.ciceksepeti.com/"


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']


dfHam=dfHam.drop_duplicates(subset=['UrunKodu'],ignore_index=True)
dfHam=dfHam.sort_values('UrunKodu',ignore_index=True)
dfSayfa3=dfSayfa3.sort_values('UrunKodu',ignore_index=True)
boyut=len(dfSayfa3)

row=0
for i in range(0,len(dfHam['UrunKodu'])):
    while dfHam.iloc[i, 1]==dfSayfa3.iloc[row,0] and row<boyut-1:
        if dfSayfa3.iloc[row,1]=='Yukseklik':
            dfHam.at[i, 'Yükseklik (cm)'] = dfSayfa3.iloc[row,2]
        elif dfSayfa3.iloc[row,1]=='Genislik':
            dfHam.at[i, 'Genişlik (cm)'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Derinlik':
            dfHam.at[i, 'Derinlik (cm)'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Renk':
            dfHam.at[i, 'Renk'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Agirlik':
            dfHam.at[i, 'Ağırlık'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Mutfak_Dolabi_Duser_Kalkar_Kapak':
            dfHam.at[i, 'Düşer Kalkar Kapak'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Cekmece_Sayisi':
            dfHam.at[i, 'Çekmece Sayısı'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Mutfak_Dolabi_Kulp_Malzeme':
            dfHam.at[i, 'Kulp Malzeme'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Mutfak_Dolabi_Ray_Ozellik':
            dfHam.at[i, 'Ray Özellik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Raf_Olcusu':
            dfHam.at[i, 'Raf Ölçüsü'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Raf_Sayisi':
            dfHam.at[i, 'Raf Sayısı'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Govde_Malzeme':
            dfHam.at[i, 'Gövde Malzeme'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kapak_Malzemesi':
            dfHam.at[i, 'Kapak Malzeme'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Mutfak_Tekstili_Pamuk_Yuzdesi':
            dfHam.at[i, 'Pamuk Yüzdesi'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Tekstili_Polyester_Yuzdesi':
            dfHam.at[i, 'Polyester Yüzdesi'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Tekstili_Yikama_Derecesi':
            dfHam.at[i, 'Yıkama Derecesi'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Paket_Icerigi':
            dfHam.at[i, 'Paket İçeriği'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Modeli':
            dfHam.at[i, 'Modeli'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Olcu':
            dfHam.at[i, 'Ölçü (cm)'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Paket_Icerigi':
            dfHam.at[i, 'Paket İçeriği'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Malzeme':
            dfHam.at[i, 'Malzeme'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Supurgelik':
            dfHam.at[i, 'Süpürgelik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Tezgah_Olculeri':
            dfHam.at[i, 'Tezgah Ölçüleri'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Ust_Modul_Derinlik':
            dfHam.at[i, 'Üst Modül Derinlik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Ust_Modul_Genislik':
            dfHam.at[i, 'Üst Modül Genişlik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Ust_Modul_Yukseklik':
            dfHam.at[i, 'Üst Modül Yükseklik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Raf_Arasi_Genislik':
            dfHam.at[i, 'Raf Arası Mesafe'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Raf_Olcusu':
            dfHam.at[i, 'Raf Ölçüsü'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Ust_Modul_Yukseklik':
            dfHam.at[i, 'Üst Modül Yükseklik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Mutfak_Dolabi_Ust_Modul_Yukseklik':
            dfHam.at[i, 'Üst Modül Yükseklik'] = dfSayfa3.iloc[row, 2]




        row=row+1



dfHam=dfHam.sort_values('UrunAdi',ignore_index=True)

#for i in range(0,len(dfHam['UrunKodu'])):
#   dfHam.at[i, 'Sıra No'] = i+1
#dfHam=dfHam.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]

#dfHam['Durum'] = pd.Series(dtype='str')
#dfHam['Kaynak'] = pd.Series(dtype='str')
dfHam.to_excel('Amerikan Servis_Final.xlsx')
