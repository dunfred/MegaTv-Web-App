from django import forms
from .models import Post, PostImage

class LoginForm(forms.Form):
    email = forms.CharField(   
        max_length=60,     
        widget=forms.TextInput(attrs={
            "type":"email",
            "id":"inputEmail",
            "class":"form-control",
            "placeholder":"Email address",
            "required" : True,
        })
    )

    password = forms.CharField(    
        max_length=60,    
        widget=forms.TextInput(attrs={
            "type":"password",
            "id":"inputPassword",
            "class":"form-control",
            "placeholder":"Password",
            "required" : True,
        })
    )

class CreatePostForm(forms.ModelForm):    
    post_title = forms.CharField(        
        widget=forms.TextInput(attrs={
            "class": "form-control authorForm",
            "placeholder": "Post Title"
        })
    )
    post_brief = forms.CharField(        
        widget=forms.TextInput(attrs={
            "class": "form-control authorForm",
            "placeholder": "Short Post Brief"
        })
    )
    post_thumbnail = forms.CharField(        
        widget=forms.TextInput(attrs={
            "class": "form-control authorForm",
            "placeholder": "Post Thumbnail"
        })
    )
    post_content = forms.CharField(        
        widget=forms.Textarea(attrs={
            "class": "form-control authorForm",
            "placeholder": "Post Body"
        })
    )        
    class Meta:
        model = Post
        fields = ("category", "post_images", "post_videos")


class CreatePostImageForm(forms.Form):
    model = PostImage
    fields = ["post_images",]

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control authorForm",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control bodyForm",
            "placeholder": "Leave a comment!"
        })
    )

class SearchForm(forms.Form):
    search_body = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control mr-sm-2",
            "placeholder": "Search",
            "aria-label":"Search",
        })
    )
