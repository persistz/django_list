from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def home_page(request):
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text', ''),
    # })
    if request.method == 'POST':
        logger.debug('Into POST')
        print("***********************")
        new_item_text = request.POST.get('item_text', '')
        Item.objects.create(text = new_item_text)
        # item = Item()
        # new_item_text = request.POST.get('item_text', '')
        # item.text = new_item_text
        # item.save()
        return redirect('/')

    else:
        print("@@@@@@@@@@@@@@@@@@@")
        logger.debug('Do not into POST')
        new_item_text = ''

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
