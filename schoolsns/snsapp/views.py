from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView
 
class PostlistView(ListView):
    """ 一覧画面を表示するView """
    template_name = 'index.html'   # 一覧画面のHTML
    model = Post                   # UserDataモデル(user_dataテーブルと紐づける)
    context_object_name = 'post_list'

    def form(self,request):
        form = PostForm()
        context = {'form':form,}
        return context

    def GetPostData(self,request):
        if request.method == 'POST':
            content =request.POST['content']        
            return content
