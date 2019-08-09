import json
import requests
from datetime import datetime

import sanitizer
from constants import SYLLABUS_URL

# import time

ALL_DATA = []


def main():
    print('\n========= start =========\n')
    s = requests.session()

    page_text = s.get(SYLLABUS_URL).text
    viewstate = sanitizer.get_viewstate(page_text)

    form_data = {
        '__VIEWSTATE': viewstate,
        'btnSearch': '以上の条件で検索'
    }

    page = get_page(s, form_data, 1)

    postback_list = sanitizer.get_postback_list(page['text'])

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


def get_page(s, form_data, index):
    print(f'\n========= page {index} =========\n')
    page_text = s.post(SYLLABUS_URL, data=form_data).text

    viewstate = sanitizer.get_viewstate(page_text)

    global ALL_DATA
    page_data_list = sanitizer.get_page_data_list(page_text)
    ALL_DATA += page_data_list

    save('../data/syllabus.json', {'data': ALL_DATA})
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
