from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.PostlistView.as_view(), name='index'),
]