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
from .models import Post,Notification

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

  

def notification(request):

    context = {
        'notifications' : Notification.objects.all(),
        'title' : 'Notification'
    }
    return render(request,'bookpark/notification.html',context)


class NotificationListView(ListView):
    model = Notification
    template_name = 'bookpark/notification.html'
    context_object_name = 'notifications'
    ordering = ['-noti_date']
    paginate_by = 5

def temp(request):
    author = request.user
    obj = request.object
    N1 = Notification(noti_name = obj.book_name,noti_body = 'You want to buy a book from ',author = author,sender_author = obj.author)
    N2 = Notification(noti_name = obj.book_name,noti_body = 'You want to sale a book to ',author = obj.author,sender_author = author.username)
    N1.save()
    N2.save()
    return render(request,'bookpark/notification.html')
