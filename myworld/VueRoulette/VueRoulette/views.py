from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

 


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def leaderboard(request):
    template = loader.get_template('leaderboard.html')
    return HttpResponse(template.render())

@csrf_exempt
def lose(request):
    template = loader.get_template('lose.html')
    if request.method == 'POST':
        record = request.POST.get('record')
    context = {
        record: record
    }
    return HttpResponse(template.render(context, request))
