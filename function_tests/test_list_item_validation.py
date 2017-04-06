from .base import FunctionalTest
import unittest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 韩梅梅访问首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # 首页刷新了，显示一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 她输入一些文字，然后再次提交，这次没问题了
        self.get_item_input_box().send_keys('I am Hanmeimei\n')
        self.check_for_rows_in_list_table('1: I am Hanmeimei')

        # 她有点儿调皮，又提交了一个空待办事项
        self.get_item_input_box().send_keys('\n')

        # 在清单页面她看到了一个类似的错误消息
        self.check_for_rows_in_list_table('1: I am Hanmeimei')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty item")

        # 输入文字之后就没问题了
        self.get_item_input_box().send_keys('He is Lilei\n')
        self.check_for_rows_in_list_table('1: I am Hanmeimei')
        self.check_for_rows_in_list_table('2: He is Lilei')
