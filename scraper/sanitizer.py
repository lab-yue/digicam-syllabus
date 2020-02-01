import re
import asyncio
import aiohttp
from lxml import html
import sys

from constants import HOST

viewstate_reg = re.compile(r'__VIEWSTATE[\s\S]+?value="(.+?)"')
subject_reg = re.compile(r'<td class="col-width-btn">([\s\S]+?)<\/tr>')
subject_field_reg = re.compile(r'<td>([\s\S]*?)</td>')
detail_link_reg = re.compile(r"window\.open\('(.+?)',")
postback_reg = re.compile(r"javascript:__doPostBack\('(.+?)'")


def get_postback_list(page_text):
    return postback_reg.findall(page_text)


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

count = 0
done = 0
async def get_page_data_list(page_text):
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            ssl=False,
            limit=10,
            force_close=True
        )) as s:
            page_text = page_text.replace('&nbsp;', '')
            tag_list = subject_reg.findall(page_text)

            async def get_tag(tag):
                global count
                global done
                count += 1
                _id = count
                subject = get_page_summary(tag)
                detail_link = HOST + detail_link_reg.findall(tag)[0]
                async with s.get(detail_link) as res:
                    detail = get_detail_data(await res.text())
                subject['detail'] = detail
                done +=1
                sys.stdout.write(f'\r\t{done} / {count} done' )    
                sys.stdout.flush()
                return subject

            page_data_list = await asyncio.gather(*(get_tag(tag) for tag in tag_list))
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
    content_rows = dom.xpath(
        "//table[@id='dgJugyoKeikaku1']//tr[not(position()=1)]")
    teacher_position = dom.xpath('//table[@id="dgKogiKyoinList"]//tr[2]/td[1]/text()')

    def separate_cells(row):
        cells = row.xpath("td")
        cells = [cell.text_content().strip() for cell in cells]
        return " ".join(cells)

    contents = [separate_cells(row) for row in content_rows]

    return {
        'day':  "\n".join(day),
        'time':  "\n".join(time),
        'teacherPosition': "\n".join(teacher_position),
        'target': "\n".join(target),
        'purpose': "\n".join(purpose),
        'keywords': keywords,
        'department': department[0],
        'teachingStyle': "\n".join(teaching_style),
        'gradePolicy': "\n".join(grade_policy),
        'finalTest': "\n".join(final_test),
        'message': "\n".join(message),
        'contents': contents
    }


def get_syllabus_count(page_txt):
    dom = html.fromstring(page_txt)
    xpath = f"//span[@id='lblTotalCnt']/text()"
    return dom.xpath(xpath)[0]
