import re

import requests
from lxml import html

from constants import HOST

viewstate_reg = re.compile(r'__VIEWSTATE[\s\S]+?value="(.+?)"')
subject_reg = re.compile('<td class="col-width-btn">([\s\S]+?)<\/tr>')
subject_field_reg = re.compile('<td>([\s\S]*?)</td>')
detail_link_reg = re.compile(r"window\.open\('(.+?)',")
postback_reg = re.compile(r"javascript:__doPostBack\('(.+?)'")


def get_postback_list(page_text):
    return postback_reg.findall(page_text)


contents


def get_page_summary(tag):

    field_list = subject_field_reg.findall(tag)
    summary = {
        'code': field_list[0],
        'title': field_list[1],
        'subtitle': field_list[2],
        'generalTitle': field_list[3],
        'time': field_list[4],
        'location': field_list[5],
        'type': field_list[6],
        'teacher': field_list[7],
        'category': field_list[8],
        'field': field_list[9],
        'year': field_list[10],
        'compulsory': field_list[11]
    }

    return summary


def get_page_data_list(page_text):
    page_text = page_text.replace('&nbsp;', '')
    tag_list = subject_reg.findall(page_text)
    page_data_list = []

    for j, tag in enumerate(tag_list):
        print(f'========= detail {j + 1} =========')

        subject = get_page_summary(tag)

        detail_link = HOST + detail_link_reg.findall(tag)[0]
        detail_text = requests.get(detail_link).text
        detail = get_detail_data(detail_text)
        subject['detail'] = detail
        print(detail)
        print(subject['title'])

        page_data_list.append(subject)
    return page_data_list


def get_viewstate(page_text):
    return viewstate_reg.findall(page_text)[0]


def get_detail_data(text):
    dom = html.fromstring(text)

    def get_text_by_id(text_id):
        xpath = f"//span[@id='{text_id}']/text()"
        return dom.xpath(xpath)

    day = get_text_by_id('lblYobi')
    time = get_text_by_id('lblJigen')
    target = get_text_by_id('lblGakushuMokuhyo')
    department = get_text_by_id('lblBusho')
    purpose = get_text_by_id('lblJugyoGaiyo')
    keywords = get_text_by_id('lblJugyoNaiyo')
    teaching_style = get_text_by_id('lblJugyoKeishiki')
    grade_policy = get_text_by_id('lblHyokaHoho')
    final_test = get_text_by_id('lblOfficeHour')
    message = get_text_by_id('lblGakuseiMessage')
    contents = dom.xpath(
        "//table[@id='dgJugyoKeikaku1']//tr[not(position()=1)]")

    return {
        'day':  "\n".join(day),
        'time':  "\n".join(time),
        'target': "\n".join(target),
        'purpose': "\n".join(purpose),
        'keywords': keywords,
        'department': department[0],
        'teachingStyle': "\n".join(teaching_style),
        'gradePolicy': "\n".join(grade_policy),
        'finalTest': "\n".join(final_test),
        'message': "\n".join(message),
        'contents': [content.text_content().strip() for content in contents]
    }
