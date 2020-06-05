import json
import logging

from bs4 import BeautifulSoup
import pandas as pd
import requests
from tqdm import tqdm


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main-hermitage-logger')


def call_api(method_name, params={},
             access_token=''):
    if params:
        params_str = '?' + '&'.join([f'{k}={v}'
                                     if isinstance(v, str)
                                     else f'{k}={",".join(v)}'
                                     for k, v in params.items()])
    url = (f'https://api.vk.com/method/{method_name}{params_str}&'
           f'v=5.103&access_token={access_token}')
    return requests.get(url).text


def write_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_members(output_filename, loop_count, count=1000):
    with open(output_filename, 'a') as f:
        for idx in tqdm(range(loop_count)):
            try:
                members_response = call_api('groups.getMembers',
                                            {'group_id': 'hermitage_museum',
                                             'offset': f'{count * idx}',
                                             'count': str(count),
                                             'fields': members_fields})
                f.write(members_response + '\n')
            except Exception as ex:
                logger.error(ex, exc_info=True)
                continue


if __name__ == '__main__':
    basic_fields = ['id', 'name', 'screen_name', 'is_closed', 'deactivated',
                    'is_admin', 'admin_level', 'is_member', 'is_advertiser',
                    'invited_by', 'type', 'photo_50', 'photo_100', 'photo_200']
    all_fields = ['activity', 'addresses', 'age_limits', 'ban_info', 'can_create_topic',
                  'can_message', 'can_post', 'can_see_all_posts', 'can_upload_doc',
                  'can_upload_video', 'city', 'contacts', 'counters', 'country',
                  'cover', 'crop_photo', 'description', 'fixed_post', 'has_photo',
                  'is_favorite', 'is_hidden_from_feed', 'is_messages_blocked',
                  'links', 'main_album_id', 'main_section', 'market',
                  'member_status', 'members_count', 'place', 'public_date_label',
                  'site', 'status', 'trending', 'verified', 'wall', 'wiki_page']
    members_fields = '''sex, bdate, city, country, photo_50, photo_100, photo_200_orig, 
                        photo_200, photo_400_orig, photo_max, photo_max_orig, online, 
                        online_mobile, lists, domain, has_mobile, contacts, connections, 
                        site, education, universities, schools, can_post, can_see_all_posts, 
                        can_see_audio, can_write_private_message, status, last_seen, common_count, 
                        relation, relatives'''.split(',')
    members_fields = [x.strip() for x in members_fields]

    basic_response = call_api('groups.getById', {'group_ids': 'hermitage_museum',
                                                 'fields': basic_fields + all_fields})
    write_json(json.loads(basic_response), 'basic_info.json')

    logger.info(f'Basic info written to file.')

    get_members('members.json', loop_count=288)
