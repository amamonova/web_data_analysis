import xmltodict
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    file = urlopen(
        'https://stepik.org/media/attachments/lesson/245681/map2.osm').read()

    xml = file.decode('utf-8')
    xml = xmltodict.parse(xml)
    num = 0

    for node in xml['osm']['node']:
        if 'tag' in node:
            if isinstance(node['tag'], list):
                for tag in node['tag']:
                    if tag['@v'] == 'fuel':
                        num += 1
            elif node['tag']['@v'] == 'fuel':
                num += 1

    print(num)