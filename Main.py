import pandas as pd
import math
import win32com.client as win32

dfHam = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\untitled6\Kilitler.xlsx')
dfSayfa3=pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\untitled6\Kilitler.xlsx','Sayfa3')


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
url="https://www.ciceksepeti.com/"


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']


dfHam=dfHam.drop_duplicates(subset=['UrunKodu'],ignore_index=True)
dfHam=dfHam.sort_values('UrunKodu',ignore_index=True)
dfSayfa3=dfSayfa3.sort_values('UrunKodu',ignore_index=True)


row=0
for i in range(0,len(dfHam['UrunKodu'])):
    while dfHam.iloc[i, 1]==dfSayfa3.iloc[row,0] and row<850:
        if dfSayfa3.iloc[row,1]=='Olcu':
            dfHam.at[i, 'Ölçüsü (yxgxd /mm)'] = dfSayfa3.iloc[row,2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Mandalli':
            dfHam.at[i, 'Mandallı'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Ayna':
            dfHam.at[i, 'Ayna'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Govde_Malzeme':
            dfHam.at[i, 'Gövde Malzeme'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Mandal_Turu':
            dfHam.at[i, 'Mandal Türü'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Fonksiyon':
            dfHam.at[i, 'Fonksiyon'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Anahtar_Ozellik':
            dfHam.at[i, 'Anahtar Özellik'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Sifreli':
            dfHam.at[i, 'Şifreli'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Agirlik':
            dfHam.at[i, 'Ağırlık (gr)'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Turu':
            dfHam.at[i, 'Ürün Tipi'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Pim_Turu':
            dfHam.at[i, 'Pim Türü'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Kam_Turu':
            dfHam.at[i, 'Kam Türü'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Yaylar':
            dfHam.at[i, 'Yaylar'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row,1]=='Kilit_Anahtar_Fonksiyon':
            dfHam.at[i, 'Fonksiyon'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Kilit_Anahtar_Kombinasyonu':
            dfHam.at[i, 'Kombinasyonu'] = dfSayfa3.iloc[row, 2]
        elif dfSayfa3.iloc[row, 1] == 'Kilit_Tuzakli':
            dfHam.at[i, 'Tuzaklı'] = dfSayfa3.iloc[row, 2]


        row=row+1



dfHam=dfHam.sort_values('UrunAdi',ignore_index=True)

#for i in range(0,len(dfHam['UrunKodu'])):
#   dfHam.at[i, 'Sıra No'] = i+1
#dfHam=dfHam.iloc[:, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]]

#dfHam['Durum'] = pd.Series(dtype='str')
#dfHam['Kaynak'] = pd.Series(dtype='str')
dfHam.to_excel('Kilitler_Final.xlsx')



dfFinal.to_excel('asd.xlsx')

#print("https://www.ciceksepeti.com/"+dfHam['Link'])
#print(dfFinal.columns)
