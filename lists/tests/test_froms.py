from django.test import TestCase
from lists.forms import ItemForm


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        # 探索式编程，fail可以引起assertionError，从而输出后面的内容
        # self.fail(form.as_p())
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validayion_for_blank_item(self):
        form = ItemForm(data={'data': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], ["You can't have an empty list item"])