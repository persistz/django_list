from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        print("*********")
        print(cls.live_server_url)
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        # 此处书中demo如下，测试报错，因为live_server_url无法正常生成，暂时不了解django中testcase的原理，使用正则绕过
        # if cls.server_url == cls.live_server_url:
        if ("127.0.0.1" in cls.server_url) or ("localhost" in cls.server_url):
            print("\n$$$$$$$$")
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_rows_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

# if __name__ == '__main__':
#     unittest.main()
