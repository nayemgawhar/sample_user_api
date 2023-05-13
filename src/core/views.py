from django.shortcuts import render
import requests


def index(request):
    get_user_infos = requests.get('https://jsonplaceholder.typicode.com/users')
    user_infos = get_user_infos.json()
    return render(request, 'index.html', {"data": user_infos})
