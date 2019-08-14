import json
import requests
from datetime import datetime

import sanitizer
from constants import SYLLABUS_URL

# import time

ALL_DATA = []
SAVE_DATA_FILE = '../data/syllabus.json'


def setup(skip_page_data=False):
    s = requests.session()

    page_text = s.get(SYLLABUS_URL).text
    viewstate = sanitizer.get_viewstate(page_text)

    form_data = {
        '__VIEWSTATE': viewstate,
        'btnSearch': '以上の条件で検索'
    }

    page = get_page(s, form_data, 1, skip_page_data)

    postback_list = sanitizer.get_postback_list(page['text'])
    return s, page, postback_list


def main():
    print('\n========= start =========\n')

    s, page, postback_list = setup()

    for i, postback in enumerate(postback_list[:int(len(postback_list) / 2)]):

        form_data = {
            '__EVENTTARGET': postback.replace('$', ':'),
            '__VIEWSTATE': page['viewstate']
        }

        page = get_page(s, form_data, i + 2)

    print(len(ALL_DATA))
    save('../data/update.json',
         {
             'updateTime': datetime.now().isoformat().split('.')[0].replace('T', ' ')
         })


def get_page(s, form_data, index, skip_page_data=False):
    page_text = s.post(SYLLABUS_URL, data=form_data).text

    viewstate = sanitizer.get_viewstate(page_text)

    if not skip_page_data:
        print(f'\n========= page {index} =========\n')
        global ALL_DATA
        page_data_list = sanitizer.get_page_data_list(page_text)
        ALL_DATA += page_data_list

        save(SAVE_DATA_FILE, {'data': ALL_DATA})
    return {
        'viewstate': viewstate,
        'text': page_text,
    }


def save(file, data):
    with open(file, 'w') as s:
        json.dump(data, s, ensure_ascii=False, indent=4)
    print('========= saved! =========')


if __name__ == '__main__':
    main()
