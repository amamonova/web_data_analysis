from urllib.request import urlopen
import re
import ssl
from collections import Counter
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')\
        .read().decode('utf-8')
    html = str(html)
    res = re.findall('<code>(.*?)</code>', html)
    c = Counter(res)
    print(c.most_common())