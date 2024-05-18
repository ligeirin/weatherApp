from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserLocale
import pdb
from .forms import ConfigureForm

import requests
import json
import re

def index(request):
    locale = UserLocale.objects.order_by('-pk').first()
    
    result = requests.get('http://api.weatherapi.com/v1/current.json?key=a5152a105dc7444ea43163315241705&q=' + locale.country + ',' + locale.federation + ',' + locale.city + '&aqi=no')
    r_status = result.status_code

    if r_status == 200:
        data = result.json()
        data['location']['formattedHour'] = re.search('\d{2}:\d{2}',data['location']['localtime']).group(0)
        data['location']['currentHour'] = int(data['location']['formattedHour'].split(':')[0])
        data['location']['timeOfDay'] = 'day'

        if data['location']['currentHour'] >= 19 or data['location']['currentHour'] < 5:
            data['location']['timeOfDay'] = 'night'
        elif data['location']['currentHour'] >= 5 and data['location']['currentHour'] <= 7:
            data['location']['timeOfDay'] = 'golden-hour'
        elif data['location']['currentHour'] >= 17 and data['location']['currentHour'] < 19:
            data['location']['timeOfDay'] = 'golden-hour'
        else:
            data['location']['timeOfDay'] = 'day'

        locale.weather = data

    context = {
        "locale": locale,
    }

    return render(request, "weather/index.html", context)

def configure(request):
    configureForm = ConfigureForm()
    return render(request, "weather/configure.html", { 'form': configureForm })


def saveConfiguration(request):
    if (request.method == 'POST'):
        form = ConfigureForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']
            federation = form.cleaned_data['federation']
            city = form.cleaned_data['city']
            UserLocale.objects.create(country=country, federation=federation, city=city)

            localeList = UserLocale.objects.order_by('country')
            context = {
                "locales": localeList,
            }
            return render(request, "weather/index.html", context)

    return render(request, "weather/configure.html", { 'form': ConfigureForm() })
