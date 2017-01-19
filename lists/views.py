from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def home_page(request):

    if request.method == 'POST':
        logger.debug('Into POST')
        print("***********************")
        new_item_text = request.POST.get('item_text', '')
        list_ = List.objects.create()
        Item.objects.create(text = new_item_text, list=list_)
        # item = Item()
        # new_item_text = request.POST.get('item_text', '')
        # item.text = new_item_text
        # item.save()
        return redirect('/lists/the-only-list-in-the-world/')

    else:
        print("@@@@@@@@@@@@@@@@@@@")
        logger.debug('Do not into POST')

    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})