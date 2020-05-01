from urllib.request import urlopen
import xmltodict
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    file = urlopen(
        'https://stepik.org/media/attachments/lesson/245678/map1.osm').read()
    xml = file.decode('utf-8')

    parsed_xml = xmltodict.parse(xml)

    tags = 0
    for node in parsed_xml['osm']['node']:
        if 'tag' in node:
            tags += 1
    no_tags = len(parsed_xml['osm']['node']) - tags
    print(f'{tags} {no_tags}')