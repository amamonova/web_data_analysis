import xmltodict
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    fin = urlopen(
        'https://stepik.org/media/attachments/lesson/245571/map1.osm')
    xml = fin.read().decode('utf-8')
    fin.close()

    parsedxml = xmltodict.parse(xml)
    print(parsedxml['osm']['node'][100]['@id'])