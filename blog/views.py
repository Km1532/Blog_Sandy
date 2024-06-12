from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .forms import CommentsForm  

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog.html', {'post_list': posts})

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'post_detail.html', {'post': post})

class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes(ip=ip_client, pos_id=pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

def about_view(request):
    return render(request, 'about.html')

def categories_view(request):
    return render(request, 'categories.html')

def tags_view(request):
    return render(request, 'tags.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return redirect('/')

def register_view(request):
    return render(request, 'register.html')

def profile_view(request):
    return render(request, 'profile.html')

def my_articles_view(request):
    return render(request, 'my_articles.html')

def create_article_view(request):
    return render(request, 'create_article.html')

def manage_announcements_view(request):
    return render(request, 'manage_announcements.html')
