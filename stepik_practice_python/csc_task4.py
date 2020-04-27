from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')\
        .read().decode()
    soup = BeautifulSoup(str(html), 'html.parser')
    res = 0
    for td in soup.find_all('td'):
        res += int(td.text)
    print(res)