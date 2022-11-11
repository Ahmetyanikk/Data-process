import pandas as pd
import glob
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os


window=tk.Tk()
window.geometry("700x350")


inputpath=""
outputpath=""


greeting = tk.Label(text="Hello, Tkinter")
greeting2 = tk.Label(text="Hello, Tkinter")
def open_file_Input():
   file = filedialog.askdirectory()
   if file:
       greeting['text']=file




def open_file_Output():
   file = filedialog.askdirectory()
   if file:
      greeting2['text']=file

def Run():
    inputpath=(greeting['text']+"/")
    outputpath=(greeting2['text']+"/")
    print(inputpath)
    excelpath = glob.glob(inputpath + "*.xlsx")
    print(excelpath)
    # ['Sıra No','PKProductId','ProductCode','Name','Linkler','İç Giyim Yaka','Malzeme','Durum','Kaynak']
    url = "https://www.ciceksepeti.com/"

    for excel in excelpath:
        filename = excel.split('\\')[-1][:-5]
        print(filename)
        dfmev = pd.read_excel(excel)
        dfmev.drop('CreatedOn', inplace=True, axis=1)
        dfmev.drop('L1_SpecList', inplace=True, axis=1)
        dfmev = dfmev.sort_values('Name', ignore_index=True)
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
        dfmev.to_excel(outputpath + f'{filename}' + "-Çıktı.xlsx", index=False)


ttk.Button(window, text="INPUT", command=open_file_Input).pack(pady=20)

ttk.Button(window, text="OUTPUT", command=open_file_Output).pack(pady=20)

ttk.Button(window, text="RUN", command=Run).pack(pady=20)


window.mainloop()
