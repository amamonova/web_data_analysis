import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('trekking2.xlsx')
    dairy = pd.read_excel('trekking2.xlsx', sheet_name='Раскладка')
    
    merged = pd.merge(dairy, df, right_on=['Unnamed: 0'],
                      left_on='Продукт')
    merged.fillna(0, inplace=True)

    merged['fats'] = merged['Вес в граммах'] * (merged['Ж на 100'] / 100)
    merged['carb'] = merged['Вес в граммах'] * (merged['У на 100'] / 100)
    merged['nuc'] = merged['Вес в граммах'] * (merged['Б на 100'] / 100)
    merged['cal'] = merged['Вес в граммах'] * (merged['ККал на 100'] / 100)

    print(merged[['fats', 'carb', 'nuc', 'cal']].sum())