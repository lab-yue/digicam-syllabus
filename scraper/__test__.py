import unittest
from constants import HOST
import constants
import sanitizer


class TestSanitizer(unittest.TestCase):
    def test_get_page_summary(self):
        __mock_text = '''
        <tr><td class="col-width-btn"><input type="submit" name="DKogiGrid:_ctl3:SelectButton" value="選択" id="DKogiGrid__ctl3_SelectButton" class="btn-submit" onclick="window.open('__URL__','WSL_SyllabusSanshoaspx','width=860,height=700,top=0,left=0,menubar=no,toolbar=no,location=no,directories=no,status=no,scrollbars=yes,resizable=yes');return false;" /></td><td>91510023</td><td>卒業制作課題(XXX)</td><td></td><td>卒業制作課題</td><td>通年</td><td>駿河台キャンパス</td><td>ゼミ</td><td>XXX</td><td>研究科目</td><td></td><td>4</td><td>必修</td></tr>
        '''
        page_summary = sanitizer.get_page_summary(__mock_text)
        __expect = {
            'code': '91510023',
            'title': '卒業制作課題(XXX)',
            'subtitle': '',
            'generalTitle': '卒業制作課題',
            'time': '通年',
            'location': '駿河台キャンパス',
            'type': 'ゼミ',
            'teacher': 'XXX',
            'catagory': '研究科目',
            'field': '',
            'year': '4',
            'compulsory': '必修'
        }

        print(page_summary)
        print(__expect)
        assert __expect == page_summary

    def test_get_view_state(self):
        __mock_text = '''
        <input type="hidden" name="__VIEWSTATE" value="SOME_BASE64_DATA" />
        '''
        view_state = sanitizer.get_viewstate(__mock_text)
        __expect = 'SOME_BASE64_DATA'

        assert __expect == view_state

    def test_get_postback_list(self):
        __mock_text = '''<tr align="Left" style="background-color:#CDF5F0;border-style:None;"><td colspan="13"><span>1</span><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl1','')">2</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl2','')">3</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl3','')">4</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl4','')">5</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl5','')">6</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl6','')">7</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl7','')">8</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl8','')">9</a><a href="javascript:__doPostBack('DKogiGrid$_ctl1$_ctl9','')">10</a></td></tr>
        '''
        postback_list = sanitizer.get_postback_list(__mock_text)
        __expect = [
            'DKogiGrid$_ctl1$_ctl1',
            'DKogiGrid$_ctl1$_ctl2',
            'DKogiGrid$_ctl1$_ctl3',
            'DKogiGrid$_ctl1$_ctl4',
            'DKogiGrid$_ctl1$_ctl5',
            'DKogiGrid$_ctl1$_ctl6',
            'DKogiGrid$_ctl1$_ctl7',
            'DKogiGrid$_ctl1$_ctl8',
            'DKogiGrid$_ctl1$_ctl9'
        ]
        assert __expect == postback_list

    def test_get_detail_data(self):

        pass


if __name__ == '__main__':
    unittest.main()
