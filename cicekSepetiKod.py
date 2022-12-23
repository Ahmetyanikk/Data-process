import pandas as pd
import glob
filename="Fantezi Aksesuar-14935-2014168"

inputpath = r"C:\\Users\\Ahmet\\PycharmProjects\\untitled6\\venv\\CicekSepetiInput\\"
outputpath = r"C:\\Users\\Ahmet\\PycharmProjects\\untitled6\\venv\\CicekSepetiOutput\\"
excelpath = glob.glob(inputpath+"*.xlsx")
#['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
url="https://www.ciceksepeti.com/"
for excel in excelpath:
    filename = excel.split('\\')[-1][:-5]
    print(filename)
    dfmev = pd.read_excel(excel)
    dfmev.drop('CreatedOn', inplace=True, axis=1)
    dfmev['Name'] = dfmev['Name'].astype(str)
    dfmev=dfmev.sort_values('Name',ignore_index=True)
    row = 0
    for i in range(0, len(dfmev['PKProductId'])):
        dfmev.at[i, 'Link'] = url + dfmev.iloc[row, 3]
        dfmev.at[i, 'Sıra No'] = i + 1
        row = row + 1
    list1 = [len(dfmev.columns) - 1]
    for i in range(0, len(dfmev.columns) - 1):
        list1.append(i)

    dfmev = dfmev.iloc[:, list1]
    dfmev['Durum'] = pd.Series(dtype='str')
    dfmev['Kaynak'] = pd.Series(dtype='str')
    dfmev.to_excel(outputpath+f'{filename}'+".xlsx", index=False)





