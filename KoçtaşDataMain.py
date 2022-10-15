import pandas as pd
import math
import win32com.client as win32

dfHam = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\untitled6\Çift Kişilik Yatak 432 -20 - Ham.xlsx')
dfSayfa3=pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\untitled6\Çift Kişilik Yatak 432 -20 - Ham.xlsx','Sayfa3')


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
url="https://www.ciceksepeti.com/"


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']


dfHam=dfHam.drop_duplicates(subset=['UrunKodu'],ignore_index=True)
dfHam=dfHam.sort_values('UrunKodu')

dfSayfa3=dfSayfa3.sort_values('UrunKodu')
row=0
for i in range(0,len(dfHam['UrunKodu'])):
    while dfHam.iloc[i, 0]==dfSayfa3.iloc[row,0] and row<4197:
        if dfSayfa3.iloc[row,1]=='Genislik':
            dfHam.at[i, 'Genişlik (cm)'] = dfSayfa3.iloc[row,2]
        elif dfSayfa3.iloc[row,1]=='Yukseklik':
            dfHam.at[i, 'Yükseklik (cm)'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Derinlik':
            dfHam.at[i, 'Derinlik (cm)'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Renk':
            dfHam.at[i, 'Renk'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Modeli':
            dfHam.at[i, 'Modeli'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Malzeme':
            dfHam.at[i, 'Malzeme'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Yatak_Yay_Sistemi':
            dfHam.at[i, 'Yay Sistemi'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Yatak_Sunger_Ozellik':
            dfHam.at[i, 'Sünger Özellik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Yatak_Dokuma_Ozellik':
            dfHam.at[i, 'Dokuma Özellik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Yatak_Yuzey_Ozellik':
            dfHam.at[i, 'Yüzey Özellik'] = dfSayfa3.iloc[row, 2]
        row=row+1



dfHam=dfHam.sort_values('UrunAdi',ignore_index=True)

for i in range(0,len(dfHam['UrunKodu'])):
    dfHam.at[i, 'Sıra No'] = i+1
dfHam=dfHam.iloc[:, [22,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]]

dfHam['Durum'] = pd.Series(dtype='str')
dfHam['Kaynak'] = pd.Series(dtype='str')
dfHam.to_excel('Final.xlsx')
