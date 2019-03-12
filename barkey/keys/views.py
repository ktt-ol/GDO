from django.shortcuts import render
from .models import key


def login(request):
    return render(request, 'keys/login.html', {})


def key_admin(request):
    return render(request, 'keys/key_admin.html', {})


def check_key(request, selectedid):
    x = selectedid
    answer = False
    try:
        barcode = key.objects.get(key_value=selectedid)
        if barcode is not None and key.is_valid(barcode):
            answer = True
        else:
            answer = False
    except:
        answer = 'you failed!'
    return render(request, 'keys/check_key.html', {'x': x, 'answer': answer})
