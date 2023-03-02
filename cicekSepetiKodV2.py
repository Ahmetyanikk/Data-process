import pandas as pd
import glob

inputpath = r"C:\\Users\\\Ahmet Yanık\\\PycharmProjects\\pythonProject\\venv\\CicekSepetiInput\\"
outputpath = r"C:\\Users\\\Ahmet Yanık\\\PycharmProjects\\pythonProject\\venv\\CicekSepetiOutput\\"

excelpath = glob.glob(inputpath + "*.xlsx")
url="https://www.ciceksepeti.com/"
for excel in excelpath:
    filename = excel.split('\\')[-1][:-5]
    print(filename)

    # Read the Excel file
    xl = pd.ExcelFile(excel)

    # Check if the file has more than one sheet
    if len(xl.sheet_names) > 1:
        # Create a new Excel file to store the other sheets
        writer = pd.ExcelWriter(outputpath + f'{filename}_OtherSheets.xlsx', engine='openpyxl')

        # Loop through each sheet in the Excel file
        for sheet in xl.sheet_names:
            # Skip the first sheet (we'll process it separately)
            if sheet == xl.sheet_names[0]:
                continue

            # Read the sheet data
            df = pd.read_excel(excel, sheet_name=sheet)

            # Save the sheet to the new Excel file
            df.to_excel(writer, sheet_name=sheet, index=False)

        # Save the new Excel file
        writer.save()

    # Process the first sheet of the Excel file
    df = pd.read_excel(excel)
    df.drop('CreatedOn', inplace=True, axis=1)
    df['Name'] = df['Name'].astype(str)
    df = df.sort_values('Name', ignore_index=True)
    df['Link'] = df['Link'].astype(str)
    row = 0
    for i in range(0, len(df['PKProductId'])):
        df.at[i, 'Link'] = url + df.iloc[row, 3]
        df.at[i, 'Sıra No'] = i + 1
        row = row + 1
    list1 = [len(df.columns) - 1]
    for i in range(0, len(df.columns) - 1):
        list1.append(i)

    df = df.iloc[:, list1]
    df['Durum'] = pd.Series(dtype='str')
    df['Kaynak'] = pd.Series(dtype='str')
    df.to_excel(outputpath + f'{filename}.xlsx', index=False)
