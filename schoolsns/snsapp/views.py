from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView,CreateView,TemplateView,FormView
from django.urls import reverse_lazy

class PostlistView(ListView):
    """ 一覧画面を表示するView """
    template_name = 'index.html'   # 一覧画面のHTML
    model = Post
    def list(self,request):
        ctx = {}
        qs = Post.objects.all()
        ctx["post_list"] = qs
        return render(request,'index.html',ctx)                  # UserDataモデル(user_dataテーブルと紐づける)

class FormPostView(CreateView):
    # modelに基となるクラスを指定
    template_name = 'create.html'
    model = Post
    # 別途定義したフォームのクラスを指定
    form_class = PostForm
    # 登録完了後の遷移ページ
    success_url = reverse_lazy('index')
    
