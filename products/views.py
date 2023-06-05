from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForm

# Create your views here.

def product_list_view(request):
  blogs = Blog.objects.all()

  context = {
    "blogs":blogs,
  }
  
  return render(request, "index.html",context)


def product_detail_view(request,id):
   blog = Blog.objects.get( id=id) 
   
   context = {
      'blog': blog,
    }
  
   return render(request, "detail.html",context)
 
def create_view(request):
  form = BlogForm()
  if request.method == 'POST':
    form = BlogForm(request.POST)
    
    if form.is_valid():
      form.save()
      
      return redirect ("products:list")
    return HttpResponse("Product created successfully!")
    
  context={
      "form":form
    }

  return render(request, "create.html",context)


def blog_update_view(request,id):
  # blog = Blog.objects.get( id=id) 
  blog = get_object_or_404(Blog,id=id)
  form = BlogForm(instance=blog)
  if request.method == 'POST':
    form = BlogForm(request.POST,instance=blog)
    
    if form.is_valid():
      form.save()
      
      return redirect ("products:list")
    return HttpResponse("Product updated successfully!")
  context={
      "form":form
    }
  return render(request, "update.html",context)

def blog_delete_view(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        blog.delete()
        return redirect("products:list")
        
    context = {
        "blog": blog
    }
    return render(request, "delete.html", context)


  