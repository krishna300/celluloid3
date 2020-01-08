from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Post
from .extra import to_data

from django.contrib.auth.decorators import login_required

def home(request):

	posts=Post.objects.all()

	context={

	"posts":posts
	}
	return render(request,'subscene/home.html',context)
    # return HttpResponse("hi django")


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

