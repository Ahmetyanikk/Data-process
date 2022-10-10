import pandas as pd
import math
import win32com.client as win32

dfHam = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\\untitled6\14911-2014144-Atlet, Külot Takımı - Ham.xlsx')
dfFinal= pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\\untitled6\Final.xlsx')

print(dfFinal.columns)
#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
dfFinal['Sıra No']=[]
dfFinal['PKProductId']=[]
dfFinal['ProductCode']=[]
dfFinal['Name']=[]
dfFinal['Linkler']=[]
dfFinal['İç Giyim Yaka']=[]
dfFinal['Malzeme']=[]
dfFinal['Durum']=[]
dfFinal['Kaynak']=[]
print(dfFinal.columns)
#dfFinal.to_excel('asd.xlsx')
