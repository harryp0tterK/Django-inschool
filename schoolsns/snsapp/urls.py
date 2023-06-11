from django.urls import path
from .views import PostlistView, CreatePost
 
urlpatterns = [
    path('', PostlistView.as_view(), name='index'),
    path('create/', CreatePost.as_view(), name='create')
]