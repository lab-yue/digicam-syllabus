import requests
import re

SYLLABUS_URL = 'https://campus.dhw.ac.jp/public/web/Syllabus/WebSyllabusKensaku/UI/WSL_SyllabusKensaku.aspx'

viewstate_reg = re.compile(r'__VIEWSTATE[\s\S]+?value="(.+?)"')
subject_reg = re.compile('<td class="col-width-btn">([\s\S]+?)<\/tr>')
subject_field_reg = re.compile('<td>([\s\S]+?)</td>')


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    s = requests.session()

    first_render_page_text = s.get(SYLLABUS_URL).text
    first_render_viewstate_token = get_viewstate_token(first_render_page_text)

    first_render_data = {
        '__VIEWSTATE': first_render_viewstate_token,
        'btnSearch': '以上の条件で検索'
    }

    page_1_text = s.post(
        SYLLABUS_URL,
        data=first_render_data).text

    get_page_data(page_1_text)


def get_viewstate_token(page_text):
    return viewstate_reg.findall(page_text)[0]


def get_page_data(page_text):
    tag_list = subject_reg.findall(page_text)

    for tag in tag_list:
        tags = subject_field_reg.findall(tag)
        print(tags)


if __name__ == '__main__':
    main()
