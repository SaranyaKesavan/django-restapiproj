from django.urls import path,re_path

from .views import (
                    UpdateModelDetailAPIView,
                    UpdateModelListAPIView
                )

urlpatterns = [
        re_path(r'^$', UpdateModelListAPIView.as_view()), # api/updates/  - List/Create
        re_path(r'^(?P<id>\d+)$', UpdateModelDetailAPIView.as_view(),)
    ]
