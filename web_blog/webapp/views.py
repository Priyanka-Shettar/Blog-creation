from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,View
from .forms import BlogForm, CommentForm
from .models import Blog, BlogComment
from django.template.loader import get_template
# Create your views here.

class DashBoard(CreateView):
    '''Creating the dasdboard for the blog '''
    def get(self,request):
        #fetching the blog form written in forms
        print("get")
        template_name = "blog_upload.html"
        form=BlogForm()
        context={
            'form':form,
            }
        return render(request,template_name,context)
    def post(self,request):
        #
        template_name = "blog_upload.html"
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('/all-blogs/')
        else:
            print(form.errors)
            print("invalid")
            context={
                'form':form,
                }
            return render(request,template_name,context)


class AllBlogView(ListView):
    model = Blog
    def get(self,request):
        template_name = "all_blog.html"
        blogs=Blog.objects.all() #returns all the blogs from blog models
        return render(request,template_name,{'blogs':blogs})

class SingleBlogView(CreateView):
    def get(self,request,pk):

        blog=Blog.objects.get(pk=pk)
        #fetching the blog form written in forms
        template_name = "single_blog.html"
        form=CommentForm()
        comments=BlogComment.objects.filter(blog=blog)
        context={
            'form':form,
            'blog':blog,
            'comments':comments
            }
        return render(request,template_name,context)

    def post(self,request,pk):
        #
        blog=Blog.objects.get(pk=pk)
        template_name = "single_blog.html"
        form=CommentForm(request.POST)
        if form.is_valid():
            print("valid")
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email_id']
            comment=form.cleaned_data['comment']
            comments,create=BlogComment.objects.get_or_create(blog=blog,first_name=first_name,
            last_name=last_name,email_id=email,comment=comment)
            comments=BlogComment.objects.filter(blog=blog)
            form=CommentForm()
            context={
                'form':form,
                'blog':blog,
                'comments':comments
                }
            return render(request,template_name,context)

        else:
            print(form.errors)
            print("invalid")
            comments=BlogComment.objects.filter(blog=blog)
            context={
                'form':form,
                'blog':blog,
                'comments':comments
                }
            return render(request,template_name,context)
