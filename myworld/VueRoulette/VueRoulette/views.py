from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

