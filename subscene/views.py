from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.http import HttpResponse
from .models import Post
from .extra import to_data
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from users.forms import CreateForm1
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib import messages
# def home(request):

# 	posts=Post.objects.all()

# 	context={

# 	"posts":posts
# 	}
# 	return render(request,'subscene/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'subscene/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-id']


class MyPosts(ListView):
    model = Post
    template_name = 'subscene/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    def get_queryset(self):
        # queryset = Post.objects.all()
        qs = super().get_queryset() 
        qs=qs.filter(author=self.request.user)
        # qs=qs.filter(author=request.username)
        # queryset = queryset.filter(author == self.request.user.username)
        return qs
  
# def create(request):
#     form = CreateForm1(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         post = form.save(commit=False)
#         # post.document = request.FILES['document']
#         # post.image = request.FILES['image']
        
#         post.save()
#         return render(request, 'subscene/detail.html', {'post': post})
#     context = {
#         "form": form,
#     }
#     return render(request, 'subscene/postform.html', context)


# 
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'image','document']
    template_name = 'subscene/postform.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def detail(request,post_id):

	post=Post.objects.get(pk=post_id)

	entitle=str(post.document)
	
	data1=to_data(entitle)
	dr=[i[2:]for i in data1]
	context={
		"data1":dr,
		"entitle":entitle,
		"post":post,
	}
	return render(request,'subscene/detail.html',context)


