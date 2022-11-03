import pandas as pd


dfHam = pd.read_excel(r'C:\Users\\Ahmet Yanık\\PycharmProjects\pythonProject\Abiye Ayakkabı-13606-2014020.xlsx')

#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
url="https://www.ciceksepeti.com/"

dfHam.drop('CreatedOn', inplace=True, axis=1)
dfHam=dfHam.sort_values('Name',ignore_index=True)

row=0
for i in range(0,len(dfHam['PKProductId'])):
    dfHam.at[i, 'Link']=url+dfHam.iloc[row,3]
    dfHam.at[i, 'Sıra No'] = i+1


dfHam=dfHam.iloc[:, [11,1,2,3,4,5,6,7,8,9,10]]
dfHam['Durum'] = pd.Series(dtype='str')
dfHam['Kaynak'] = pd.Series(dtype='str')
dfHam.to_excel('Abiye Ayakkabı-13606-2014020_Final.xlsx',index=False)
