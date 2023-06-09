from django.shortcuts import render
from .forms import PostForm
 
def index(request):
    form = PostForm()
    context = {'form':form,}
    return render(request, 'index.html', context)

def GetPostData(request):
    if request.method == 'POST':
        content =request.POST['content']        

        return render(request, 'index.html', params)
