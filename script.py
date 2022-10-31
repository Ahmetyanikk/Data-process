import pandas as pd
import glob
## excel dosyalarının bulunduğu klasörün dizin bilgisi inputpath kısmına yazılacak
## oluşturulan çıktıların kaydedileceği dizin outputpath kısmına yazılacak
inputpath = r"C:\\Users\\Ahmet\\PycharmProjects\\untitled6\\venv\\inputexcel\\"
outputpath = r"C:\\Users\\Ahmet\\PycharmProjects\\untitled6\\venv\\outputexcel\\"
excelpath = glob.glob(inputpath+"*.xlsx")
print(excelpath)
for excel in excelpath:
    print(excel)
    filename = excel.split('\\')[-1][:-5]
    dfmev = pd.read_excel(excel)
    dfmev = dfmev.drop(['Sıra No'], axis=1)
    dfsonuc = pd.DataFrame(columns=['UrunKodu','UrunAdi','SiniflandirmaKod','SiniflandirmaDeger'])
    kolnum = len(dfmev.columns)
    rownum = dfmev.shape[0]
    count = 0
    for a in range(0, rownum):
        for i in range(0,kolnum):
            if i+2 <kolnum:
                dfsonuc.loc[count, 'UrunKodu'] = dfmev.iloc[a, 0]
                dfsonuc.loc[count, 'UrunAdi'] = dfmev.iloc[a, 1]
                dfsonuc.loc[count, 'SiniflandirmaKod'] = dfmev.columns[i+2].replace("( ","(").replace(" ","_")
                dfsonuc.loc[count, 'SiniflandirmaDeger'] = dfmev.iloc[a,i+2]
                count+=1

    dfsonuc.to_excel(outputpath+f'{filename}'+".xlsx", index=False)
