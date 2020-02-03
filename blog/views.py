from django.shortcuts import render, redirect, reverse
from .models import Post, Category, Comment
from .forms import CommentForm, SearchForm
from django.http import HttpResponseRedirect

# Create your views here.
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
    template    = "blog_post_list.html"
    
    if search_funtion(request, context) != False:
        HttpResponseRedirect(reverse('blog-posts'))
        return render(request,"blog_post_list.html", search_funtion(request, context))
    else:
        return render(request, template, context)

def blog_detail(request, slug):          
    post = Post.objects.get(slug=slug)        
    related_posts = Post.objects.filter(category__name__startswith=post.category.values()[0]['name']).order_by('-created_on')
    form = CommentForm()
    search_form = SearchForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            form = CommentForm()
            return HttpResponseRedirect(reverse('blog-posts-details', args=[post.slug]))

    comments = Comment.objects.filter(post=post)
    number_of_commments = str(len(comments)) + " Comment" if len(comments) == 1 else str(len(comments)) + " Comments"

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
        return render(request,"blog_post_list.html", search_funtion(request, context))
    else:
        return render(request, template, context)

def blog_category(request, category):
    posts = Post.objects.filter(category__name__contains=category).order_by('-created_on')
    search_form = SearchForm()
    context = {
        "search_form":  search_form,
        "category":     category,
        "posts":        posts,
    }
    template = "blog_category.html"

    if search_funtion(request, context) != False:
        return render(request,"blog_post_list.html", search_funtion(request, context))
    else:
        return render(request, template, context)


def post_full_page(request):      
    obj = Post.objects.filter()
    search_form = SearchForm()
    context = {
        "search_form":  search_form,
        'obj':          obj[1],
        'objs':         obj}      

    template = "post_full_page.html"

    if search_funtion(request, context) != False:
        return render(request,"blog_post_list.html", search_funtion(request, context))
    else:
        return render(request, template, context)

def location_map(request):      
    return render(request, "map.html", {})

def sign_up(request):      
    return render(request, "signup.html", {})    

def sign_in(request):      
    return render(request, "signin.html", {})

def image_post(request):      
    return render(request, "images.html", {})

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

