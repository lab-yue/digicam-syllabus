import json
import hashlib

from main import save


def hash(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()[:8]


def build():
    teacher_list = []
    search_data = []

    with open('../data/syllabus.json', 'r') as f:
        syllabus = json.load(f)
    for subject in syllabus['data']:
        origin_detail = subject['detail']

        detail_list = []
        detail_list.append(subject['title'])
        detail_list.append(origin_detail['day'])
        detail_list.append(origin_detail['target'])
        detail_list.append(origin_detail['purpose'])
        detail_list.append(origin_detail['teachingStyle'])
        detail_list.append(origin_detail['gradePolicy'])
        detail_list.append(origin_detail['finalTest'])
        detail_list.append(origin_detail['message'])
        detail_list.append(" ".join(origin_detail['keywords']))
        detail_list.append(" ".join(origin_detail['contents']))

        if (subject['teacher'] not in teacher_list):
            search_data.append({
                'text': subject['teacher'],
                'type': 'teacher',
                'title': '教員',
                'id': hash(f'teacher:{subject["teacher"]}'),
            })

            teacher_list.append(subject['teacher'])

        search_data.append({
            'text': " ".join(detail_list).strip(),
            'type': 'subject',
            'title': subject['title'],
            'id': subject['code']
        })

    save('../data/search.json',
         {
             'data': search_data
         })


if __name__ == '__main__':
    build()
