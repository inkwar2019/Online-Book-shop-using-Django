from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post

# Create your views here.

# def home(request):
#     context = {
#         'posts' : Post.objects.all(),
#         'title' : 'Home'
#     }
#     return render(request,'bookpark/home.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'bookpark/home.html'
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 5


class PostDetailView(DetailView): 
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['book_name','book_description']

    def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['book_name','book_description']

    def form_valid(self, form):
         form.instance.author = self.request.user
         return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

  

def about(request):
    context = {
        'title' : 'Notifications'
    }
    return render(request,'bookpark/about.html',context)