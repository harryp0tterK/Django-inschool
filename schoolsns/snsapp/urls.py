from django.urls import path
from .views import PostlistView,FormPostView
from snsapp import views
 
urlpatterns = [
    path('', PostlistView.as_view(), name='index'),
    path('create/', FormPostView.as_view(), name='create')
]