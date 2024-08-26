#from django.shortcuts import render
from django.contrib import messages
from typing import Any
from django.views.generic import TemplateView, FormView, DetailView # Create your views here.
from .models import post
from .form import PostForm

class HomePageView (TemplateView):
    template_name = "base.html"
    
    def get_context_data(self, **kwargs: Any) : 
        context = super().get_context_data(**kwargs) # get data from kwargs 
        #context ['my_thing'] = "hello world : this dynamic" # add variable 
        context ['posts'] = post.objects.all().order_by('-id')
        return context # return to context
    
class postDetailView (DetailView):
    template_name = "detail.html"
    model = post

class AddPostView (FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object = post.objects.create(
        text=form.cleaned_data['text'],
        image=form.cleaned_data['images']  
    )
        messages.add_message(self.request, messages.SUCCESS, "Post successful.")
        return super().form_valid(form)

