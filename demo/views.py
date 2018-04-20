from django.shortcuts import render, redirect
from demo.models import Blog

def index(request):
	blogs = Blog.objects.all()
	context = {
		'blogs': blogs
	}
	return render(request, 'index.html', context) 

def blog_delete(request, blog_id):
	blog = Blog.objects.get(id = blog_id)
	blog.delete()
	return redirect('index')

def blog_detail(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	context = {
		'blog': blog
	}
	return render(request, 'blog_detail.html', context)

def blog_edit(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    if request.method == "POST":
    	title = request.POST['title']
    	body = request.POST['body']
    	blog.title = title
    	blog.body = body  
    	
    	blog.save()
    	return redirect('index') 
    else:
    	return render(request, 'blog_edit.html', {"blog": blog})

def blog_add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		body = request.POST['body']
		blog = Blog(title=title, body=body)
		
		blog.save()
		return redirect('index')
	else:
		return render(request, 'blog_add.html')


# Create your views here.
