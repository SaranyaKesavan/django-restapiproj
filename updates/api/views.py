import json
from django.views.generic import View
from django.http import HttpResponse

from updates.models import Update as UpdateModel
from updates.forms import UpdateModelForm

from .mixins import CSRFExemptMixin

from restapiproj.mixins import HttpResponseMixin



 # Creating, Updating, Deleting, Retrieving

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin,View):
    '''
    Retrieve, Update, Delete ==>> Object
    '''
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        data = json.dumps({"message" : "Not allowed, please use the /api/updates/ endpoint"})
        return self.render_to_response(data, status=400)

    def put(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data, status=400)

    def delete(self, request, *args, **kwargs):
        data = {}
        return self.render_to_response(data, status=403)

class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin,View):
    '''
    List View
    Create View
    '''
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        print(request.POST) 
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)   
            return self.render_to_response(data, status=400)
        data = json.dumps({"message":"Unknown Data"})
        return self.render_to_response(data, status=400) # 400 ==> Bad Request

    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message":"You don't have permission to delete the data!"})
        return self.render_to_response(data, status=403) # 403 ==> Forbidden