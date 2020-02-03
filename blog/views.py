from django.shortcuts import render, redirect, reverse
from .models import BlogUser, Post, PostImage, Category, Comment
from .forms import CommentForm, SearchForm, CreatePostForm, CreatePostImageForm, LoginForm
from django import forms
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required(login_url="../../login/")
def blog_create(request):   
    post_form = CreatePostForm()
    post_img_form = CreatePostImageForm()

    context = {
        "postform":post_form,
        "postimgs":post_img_form,
    }

    return render(request, "blog_create.html", context)

def search_funtion(request, context, *args, **kwargs):        
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search = search_form.cleaned_data["search_body"] 
            print("Search:", search)
            search_results = Post.objects.filter(post_title__contains=search)                         
            context["search_results"] = search_results
            print("Search Results:",context["search_results"])
            
            #render(request,"blog_post_list.html", context)
            #HttpResponseRedirect(reverse('blog-posts'))
            search_form = SearchForm()
            return context           
        else:
            return False
    else:
        return False

def blog_post(request):
    obj = Post.objects.filter()    
    search_form = SearchForm()
    #return HttpResponseRedirect(reverse('blog-searches', args=["-".join(search.lower())]))
    template_name = "base.html"        
    reversed_obj = obj[::-1]
    context = {'obj':reversed_obj[:3],
               "search_form":search_form,}
    search_funtion(request, context)               

    return render(request, template_name, context)

def list_post(request):      
    search_form = SearchForm()    
    context     = {"search_form":search_form}
    template    = "search_results.html"
    
    if search_funtion(request, context) != False:
        HttpResponseRedirect(reverse('blog-posts'))
        return render(request,"search_results.html", search_funtion(request, context))
    else:
        return render(request, template, context)

def blog_detail(request, slug):          
    post = Post.objects.get(slug=slug)        
    related_posts = Post.objects.filter(category__name__startswith=post.category.values()[0]['name']).order_by('-created_on')
    form = CommentForm()
    search_form = SearchForm()    
    comments = Comment.objects.filter(post=post)
    number_of_commments = len(comments)

    context = {
        "post":                 post,
        "comments":             comments,
        "form":                 form,        
        "search_form":          search_form,
        "related_posts":        related_posts,
        "number_of_commments":  number_of_commments,
    }
    template = "blog_details.html"
    
    if search_funtion(request, context) != False:
        HttpResponseRedirect(reverse('blog-posts'))
        return render(request,"search_results.html", search_funtion(request, context))
    else:
        return render(request, template, context)

def blog_category(request, category):
    posts = Post.objects.filter(category__name__startswith=category)    
    print(category)
    print(posts)
    search_form = SearchForm()
    context = {
        "posts":        posts,
    }
    template = "blog_category.html"

    if search_funtion(request, context) != False:
        return render(request,"search_results.html", search_funtion(request, context))
    else:
        return render(request, template, context)


def post_full_page(request):      
    obj = Post.objects.filter()
    search_form = SearchForm()
    context = {
        "search_form":  search_form,
        'obj':          obj[1],
        'objs':         obj}      

    template = "search_results.html"

    if search_funtion(request, context) != False:
        return render(request,"search_results.html", search_funtion(request, context))
    else:
        return render(request, template, context)

def location_map(request):      
    return render(request, "map.html", {})

def sign_up(request):      
    return render(request, "user_signup.html", {})    

def sign_in(request):      
    form = LoginForm()
    if request.method == "POST":        
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            users = BlogUser.objects.all()
            form_email = form.cleaned_data["email"]
            form_password = form.cleaned_data["password"]
            
            try:
                #user = BlogUser.objects.get(email=form_email, password=form_password)
                #print(f"User: {user.username} \nPass: {user.password}")
                user = authenticate(email=form_email, password=form_password)
                print(user)
                login(request, user)
                print("User logged in")
                return reverse("blog-create")
            except Exception:
                raise forms.ValidationError("No such user exists")
                pass

    context = {
        "form":form,
    }
    return render(request, "user_signin.html", context)

def image_post(request):      
    exFormSet = modelformset_factory(PostImage, fields=('post_images','post'), extra=3)

    if request.method == "POST":        
        form = exFormSet(request.POST)
        print("Saving Form")
        instances = form.save(commit=False)        

        for instance in instances:
            if instance is not None:
                print(request.POST)
                instance.save()
    form = exFormSet(queryset=PostImage.objects.none())

    return render(request, "images.html", {"form":form})

def intro(request):      
    return render(request, "intro.html", {})
 
def video_post(request):      
    obj = Post.objects.filter()[0]
    return render(request, "video.html", {'obj':obj})


'''
def blog_post(request):      
    return render(request, "counter.html", {})



def blog_post(request):      
    return render(request, "subscribe.html", {})

'''
