from django.shortcuts import render

def login(request):
    return render(request, 'keys/login.html', {})


def key_admin(request):
    return render(request, 'keys/key-admin.html', {})
