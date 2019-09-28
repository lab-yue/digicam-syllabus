import asyncio
import aiohttp

import sanitizer
import store
from main import setup
from constants import SYLLABUS_URL


def get_local_len():
    db = store.Instance()
    db.load()
    return len(db.data)


async def check_len():
    print('=========  check! =========')
    local_len = get_local_len()

    s = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            ssl=False,
            limit=50,
            force_close=True
        ))

    async with s.get(SYLLABUS_URL) as res:
        viewstate = sanitizer.get_viewstate(await res.text())
        form_data = {
            '__VIEWSTATE': viewstate,
            'btnSearch': '以上の条件で検索'
        }

    async with s.post(SYLLABUS_URL, data=form_data) as res:
        text = await res.text()
        web_len = int(sanitizer.get_syllabus_count(text))

    await s.close()

    is_equal = local_len == web_len
    message = 'same.' if is_equal else 'should update.'

    print(f'''
    local_len, {local_len}
    web_len, {web_len}
    {message}
    ''')

    return is_equal

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_len())
