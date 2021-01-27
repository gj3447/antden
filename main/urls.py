from django.urls import path
from . import views

name = 'main'
urlpatterns = [
    path('key/<int:code>/',views.array_url),
    path('page/<int:code>/',views.index)
]