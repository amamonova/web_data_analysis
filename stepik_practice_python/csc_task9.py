import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('trekking1.xlsx')
    df.fillna(0, inplace=True)
    df = df.sort_values(by=['ККал на 100', 'Unnamed: 0'],
                        ascending=[False, True])
    for val in df['Unnamed: 0'].values:
        print(val)