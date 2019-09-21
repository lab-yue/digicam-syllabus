import asyncio
from concurrent.futures import ProcessPoolExecutor
import json
import aiohttp
import requests
from datetime import datetime

import sanitizer
import store
from constants import SYLLABUS_URL, HOST

async def setup():
    # async with aiohttp.ClientSession() as s:
    s =  aiohttp.ClientSession()

    async with s.get(SYLLABUS_URL) as res:
        viewstate = sanitizer.get_viewstate(await res.text())
        form_data = {
            '__VIEWSTATE': viewstate,
            'btnSearch': '以上の条件で検索'
        }
        async with s.post(SYLLABUS_URL, data=form_data) as res:
            text = await res.text()
            data_list = await sanitizer.get_page_data_list(text)
            db.collect(data_list)
            # cookies = {}
            # cookies[SID_KEY] = res.cookies.get(SID_KEY)
            postback_list = sanitizer.get_postback_list(text)
            viewstate = sanitizer.get_viewstate(text)
            return s, viewstate, postback_list


async def main():
    print('\n========= start =========\n')
    #tasks = []
    s, viewstate, postback_list = await setup()

    for postback in postback_list[:int(len(postback_list) / 2)]:
        task = {
            '__EVENTTARGET': postback.replace('$', ':'),
            '__VIEWSTATE': viewstate
        }
        await get_page(s, task)
        # await get_page(cookies, task)
        # tasks.append(task)

    # This is faster but it will cause server connection error
    # await asyncio.gather(*(get_page(cookies, task) for task in tasks))

    await s.close()
    db.save('../data/update.json',
          {
              'updateTime': datetime.now().isoformat().split('.')[0].replace('T', ' ')
          })
    db.build_search_data()
    print('\n========= end =========\n')


async def get_page(s, form_data):
    #async with aiohttp.ClientSession(cookies=cookies) as s:
    async with s.post(SYLLABUS_URL, data=form_data) as res:
        text = await res.text()
        data_list = await sanitizer.get_page_data_list(text)
        db.collect(data_list)


if __name__ == '__main__':

    db = store.Instance()
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor(max_workers=10)
    loop.set_default_executor(executor)
    loop.run_until_complete(main())