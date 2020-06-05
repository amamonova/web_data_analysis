import json

import pandas as pd


def get_dataframe(json_data_filename):
    with open(json_data_filename, 'r') as f:
        data = f.readlines()

    columns_names = ['id', 'first_name', 'last_name', 'is_closed', 'can_access_closed',
                     'sex', 'domain', 'bdate', 'city', 'country', 'photo_50', 'photo_100',
                     'photo_200', 'photo_200_orig', 'photo_max', 'photo_max_orig',
                     'has_mobile', 'online', 'can_post', 'can_see_all_posts',
                     'can_see_audio', 'can_write_private_message', 'site', 'status',
                     'last_seen', 'common_count', 'photo_400_orig', 'deactivated', 'skype',
                     'instagram', 'university', 'university_name', 'faculty', 'faculty_name',
                     'graduation', 'education_form', 'relation', 'universities', 'schools',
                     'relatives', 'facebook', 'facebook_name', 'twitter', 'education_status',
                     'mobile_phone', 'home_phone', 'online_app', 'online_mobile',
                     'relation_partner', 'livejournal', 'status_audio']
    members_df = pd.DataFrame(columns=columns_names)

    for data_row in data:
        items = json.loads(data_row)['response']['items']
        members_df = members_df.append(pd.DataFrame(items))

    return members_df


def save_csv(df, output_filename='result.csv'):
    df.to_csv(output_filename)


if __name__ == '__main__':
    save_csv(get_dataframe('members.json'))