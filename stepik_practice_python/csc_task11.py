import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    df = pd.read_excel(
        'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx')
    dairy = pd.read_excel(
        'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx',
        sheet_name='Раскладка', index_col=False)

    merged = pd.merge(dairy, df, right_on=['Unnamed: 0'],
                      left_on='Продукт')
    merged.fillna(0, inplace=True)

    merged['fats'] = merged['Вес в граммах'] * (merged['Ж на 100'] / 100)
    merged['carb'] = merged['Вес в граммах'] * (merged['У на 100'] / 100)
    merged['nuc'] = merged['Вес в граммах'] * (merged['Б на 100'] / 100)
    merged['cal'] = merged['Вес в граммах'] * (merged['ККал на 100'] / 100)

    res = pd.DataFrame()
    for item in ['cal', 'nuc', 'fats', 'carb']:
        res = pd.concat([res, merged.groupby('День')[item].sum()], axis=1)

    print(res.astype(int))