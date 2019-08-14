import sanitizer
import json
from main import setup, SAVE_DATA_FILE


def get_local_len():
    local_data = None
    with open(SAVE_DATA_FILE) as f:
        local_data = json.load(f)
    return len(local_data['data'])


def check_len():
    print('=========  check! =========')
    local_len = get_local_len()
    _, page, _ = setup(skip_page_data=True)
    web_len = sanitizer.get_syllabus_count(page['text'])
    is_equal = local_len == web_len
    message = 'same.' if is_equal else 'should update.'
    print(f'''
    local_len, {local_len}
    web_len, {web_len}
    {message}
    ''')
    return is_equal


if __name__ == '__main__':
    check_len()
