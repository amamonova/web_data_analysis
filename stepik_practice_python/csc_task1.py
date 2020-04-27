from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    html = urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')\
        .read().decode('utf-8')
    if str(html).count('Python') > str(html).count('C++'):
        print('Python')
    else:
        print('C++')