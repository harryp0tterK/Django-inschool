from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,CreateView
 
class PostlistView(ListView):
    """ 一覧画面を表示するView """
    template_name = 'index.html'   # 一覧画面のHTML
    model = Post                   # UserDataモデル(user_dataテーブルと紐づける)
    context_object_name = 'post_list'

class CreatePost(CreateView):
    template_name = 'create.html'
    
