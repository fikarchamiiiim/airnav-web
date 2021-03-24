from django.urls import path
from .views import IndexMap

urlpatterns = [
    path('', IndexMap.as_view(), name="index_map"),
]
