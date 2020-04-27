import io
from urllib.request import urlretrieve
import pandas as pd
import zipfile
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
    urlretrieve(url, 'rogaikopyta')
    zf = zipfile.ZipFile('rogaikopyta')

    res = pd.DataFrame(columns=['Name', 'Salary'])
    for file in zf.namelist():
        xl = zf.read(file)
        temp = pd.read_excel(io.BytesIO(xl))

        name = temp['Unnamed: 1'][0]
        salary = temp['Unnamed: 3'][0]

        res = res.append({'Name': name, 'Salary': salary}, ignore_index=True)

    res = res.sort_values(by='Name')
    res.Salary = res.Salary.astype(int)

    with pd.option_context('display.max_rows', None, 'display.max_columns',
                           None):
        print(res.to_string(index=False))