import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('salaries.xlsx')
    df = df.set_index('Unnamed: 0')
    print(df.mean())