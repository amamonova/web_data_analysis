import json
import logging
import time

import pandas as pd
from tqdm import tqdm

from get_info import call_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main-hermitage-logger')


def get_group(output_filename, user_id, loop_count=10, count=1000, extended=1):
    groups_fields = ('city, country, place, description, wiki_page, '
                    'members_count, counters, start_date, finish_date, '
                    'can_post, can_see_all_posts, activity, status, '
                    'contacts, links, fixed_post, verified, site, can_create_topic').split(',')
    groups_fields = [x.strip() for x in groups_fields]

    with open(output_filename, 'a') as f:
        for idx in range(loop_count):
            try:
                time.sleep(0.5)
                response = call_api('groups.get',
                                            {'user_id': user_id,
                                             'offset': f'{count * idx}',
                                             'count': str(count),
                                             'fields': groups_fields,
                                             'extended': str(extended)})
                if 'response' in response:
                    if len(json.loads(response)['response']['items']) != 0:
                        f.write(response + '\n')
                    else:
                        break
                else:
                    with open(f'errors_{output_filename}', 'a') as err_out:
                        err_out.write(response + '\n')
                        break

            except Exception as ex:
                logger.error(ex, exc_info=True)
                continue


if __name__ == '__main__':
    df = pd.read_csv('data/result.csv')
    sample = df[df.sex == 1].sample(frac=1, random_state=42)[:2500]\
        .append(df[df.sex == 2].sample(frac=1, random_state=42)[:2500])
    for user_id in tqdm(sample['id']):
        get_group('groups_by_users.json', str(user_id))