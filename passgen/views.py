from django.shortcuts import render, HttpResponse 
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def passgen(request):
    try:
        if request.GET.get('uppercase') == None and request.GET.get('lowercase') == None and request.GET.get('digits') == None and request.GET.get('symbol') == None:
            return JsonResponse({'error': 'Please select at least one character type.'})
    except Exception as e:
        return JsonResponse({'error': str(e)})  
    char = list('')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('lowercase'):
        char.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbol'):
        char.extend(list('!@#$%^&*()_+~'))

    length = int(request.GET.get('length',10))

    password = ''
    for x in range(length):
        password += random.choice(char)
    return render(request, 'password.html', {'password': password})
  
