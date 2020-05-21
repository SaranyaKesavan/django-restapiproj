from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize

from restapiproj.mixins import JsonResponseMixin

from .models import Update

import json     #imports from python not from django

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

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj], fields=('user', 'content'))
        json_data = obj.serialize()
        # data = {
        #     "user" : obj.user.username,
        #     "content" : obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        #json_data = json.dumps(data)
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
