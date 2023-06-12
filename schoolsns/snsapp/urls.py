from django.urls import path
from .views import PostlistView
from snsapp import views
 
urlpatterns = [
    path('', PostlistView.as_view(), name='index'),
    path('create/', views.post, name='create')
]