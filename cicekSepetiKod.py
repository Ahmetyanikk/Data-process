import pandas as pd
import glob
filename="Fantezi Aksesuar-14935-2014168"
dfHam = pd.read_excel(r'C:\Users\\Ahmet Yanık\\PycharmProjects\pythonProject\\Tesettür Namaz Elbise-15031-2014205.xlsx')

#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
url="https://www.ciceksepeti.com/"

dfHam.drop('CreatedOn', inplace=True, axis=1)
dfHam=dfHam.sort_values('Name',ignore_index=True)

row=0
for i in range(0,len(dfHam['PKProductId'])):
    dfHam.at[i, 'Link']=url+dfHam.iloc[row,3]
    dfHam.at[i, 'Sıra No'] = i+1
    row=row+1

list1=[len(dfHam.columns)-1]
for i in range(1,len(dfHam.columns)-1):
    list1.append(i)

dfHam=dfHam.iloc[:, list1]
dfHam['Durum'] = pd.Series(dtype='str')
dfHam['Kaynak'] = pd.Series(dtype='str')
dfHam.to_excel('Tesettür Namaz Elbise-15031-2014205_Final.xlsx',index=False)
