import json
from django.conf import settings
from django.db import models
from django.core.serializers import serialize

def upload_update_image(instance, filename):
    return f"update/{instance.user}/{filename}"

#To customize serialization
class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     return serialize("json", qs, fields=('user', 'content', 'image'))   

#Completely inefficient way
#  def serialize(self):
#         qs = self
#         final_array = []
#         for obj in qs:
#             struct  = json.loads(obj.serialize())
#             final_array.append(struct)
#         return json.dumps(final_array)

    def serialize(self):
        list_values = list(self.values("id", "user", "content", "image"))
        return json.dumps(list_values)
#To serialize complete queryset   
class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)
class Update(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content   = models.TextField(blank=True, null=True)
    image     = models.ImageField(upload_to=upload_update_image, blank=True, null=True) 
    updated   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager() 

    def __str__(self):
        return self.content or ""

    #To serialize individual instance
    def serialize(self):
    #    json_data = serialize("json", [self], fields=('user', 'content', 'image'))
    #    struct = json.loads(json_data)
    #    print(struct)
        img = ""
        if self.image:
            img = self.image.url
        data = {
            'id' : self.id,
            'content' : self.content,
            'user' : self.user.id,
            'image' : img
        }
        json_data = json.dumps(data)
        return json_data