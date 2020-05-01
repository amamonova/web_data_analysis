    import xmltodict
    from urllib.request import urlopen
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    
    
    def number_of_objects(xml_dict, obj_name, area_type='node'):
        result_num = 0
        for node in xml_dict['osm'][area_type]:
            if 'tag' in node:
                if isinstance(node['tag'], list):
                    for tag in node['tag']:
                        if tag['@v'] == obj_name:
                            result_num += 1
                elif node['tag']['@v'] == obj_name:
                    result_num += 1
        return result_num
    
    
    if __name__ == '__main__':
        file = urlopen(
            'https://stepik.org/media/attachments/lesson/245681/map2.osm').read()
        xml = file.decode('utf-8')
        xml = xmltodict.parse(xml)
        num = 0
    
        for area_t in ['node', 'way']:
            num += number_of_objects(xml, 'fuel', area_t)
    
        print(num)