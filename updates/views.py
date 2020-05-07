from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from restapiproj.mixins import JsonResponseMixin
from .models import Update
import json #imports from python not from django

#def detail_view(request):
    #return render()  # return JSON data 
    #return HttpResponse(get_template().render({}))


def json_example_view(request):
    '''
    This is URI -- fro rest api
    '''
    data = {
         "count" : 1000,
         "content" : "pure django api example json"
    }
    #json_data = json.dumps(data)
    return JsonResponse(data)
    #return HttpResponse(json_data,content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kargs):
        data = {
            "count" : 1000,
            "content" : "pure django api CBV"
        }
        return JsonResponse(data)
        
class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count" : 1000,
            "content" : "some new content CBV2"
        }
        return self.render_to_json_response(data)