import pandas as pd
import math
import win32com.client as win32

dfHam = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\\untitled6\14911-2014144-Atlet, Külot Takımı - Ham.xlsx')
dfFinal= pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\\untitled6\Final.xlsx')

url="https://www.ciceksepeti.com/"


#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
dfFinal['Sıra No']=[]
dfFinal['PKProductId']=[]
dfFinal['ProductCode']=[]
dfFinal['Name']=[]
dfFinal['Linkler']=[]
dfFinal['2000411']=[]
dfFinal['İç Giyim Yaka']=[]
dfFinal['2000416']=[]
dfFinal['Malzeme']=[]
dfFinal['Durum']=[]
dfFinal['Kaynak']=[]
for i in range(0,len(dfHam['Name'])):
    dfFinal.at[i, 'PKProductId'] = dfHam.iloc[i, 0]
for i in range(0,len(dfHam['Name'])):
    dfFinal.at[i, 'Sıra No'] = i+1
for i in range(0,len(dfHam['Name'])):
    dfFinal.at[i, 'ProductCode'] = dfHam.iloc[i, 1]
for i in range(0,len(dfHam['Name'])):
    dfFinal.at[i, 'Name'] = dfHam.iloc[i, 2]
for i in range(0,len(dfHam['Name'])):
    dfFinal.at[i, 'Linkler'] = url+dfHam.iloc[i,3]



dfFinal.to_excel('asd.xlsx')

#print("https://www.ciceksepeti.com/"+dfHam['Link'])
#print(dfFinal.columns)
