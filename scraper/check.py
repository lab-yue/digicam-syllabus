import asyncio
import aiohttp
import os
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

    is_equal = local_len == web_len
    message = 'same.' if is_equal else 'should update.'

    info = f'''
    local_len, {local_len}
    web_len, {web_len}
    {message}
    '''

    print(info)

    DISCORD_WEB_HOOK = os.environ.get('DISCORD_WEB_HOOK', '')
    if DISCORD_WEB_HOOK:
        await s.post(DISCORD_WEB_HOOK, data={'content': message})
    else:
        print('skip notify')

    await s.close()

    return is_equal

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(check_len())
