from django.test import TestCase
from lists.forms import ItemForm
from lists.models import Item, List

class ItemFormTest(TestCase):

    def test_form_renders_text_input(self):
        form = ItemForm()
        # 探索式编程，fail可以引起assertionError，从而输出后面的内容
        # self.fail(form.as_p())
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_item(self):
        form = ItemForm(data={'data': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], ["You can't have an empty list item"])

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'do me'})
        new_item = form.save(for_list = list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)
