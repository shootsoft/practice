import os
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FactualService

from factual import Factual


def find(request):

    if 'location' not in request.GET or 'type' not in request.GET :
        data = {'error': True, 'message':'Missing parameters'}
    else:
        location = request.GET['location']
        type = request.GET['type']
        try:

            factual_service = FactualService()
            data = factual_service.search(type, location)
        except ValueError as err:
            data = {'error': True, 'message': err.message}

    return JsonResponse(data, safe=False)

@csrf_exempt
def recommend(request):
    data=[]
    group = None

    if 'location' not in request.GET or request.method != 'POST' or request.body == None:
        data = {'error': True, 'message':'Missing parameter or error method or error body'}
    else:
        location = request.GET['location']
        try:
            group = json.loads(request.body)
            factual_service = FactualService()
            data = factual_service.recommend(location, group)
        except ValueError as err:
            data = {'error': True, 'message': err.message}

    return JsonResponse(data, safe=False)


