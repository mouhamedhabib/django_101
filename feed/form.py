from django import forms

class PostForm (forms.Form):
    images = forms.ImageField()
    text = forms.CharField(label="description")
    fields = ['text', 'image']
    
    