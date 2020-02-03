from django.urls import path
from .views import (intro,
                    blog_post, 
                    list_post, 
                    blog_detail,
                    blog_category,
                    post_full_page,
                    location_map,
                    sign_up,
                    sign_in,
                    image_post,
                    video_post)
urlpatterns = [
    path('',                     blog_post,         name='blog-home'),
    path('blog/',                list_post,         name='blog-posts'),
    path('blog/<str:slug>/',     blog_detail,       name='blog-posts-details'),
    path('blog/<str:category>/', blog_category,     name='blog-category'),
    #path('blog/searches/',       blog_category,     name='blog-searches'),
    path('blog/all',             post_full_page,    name='all-blog-posts'),
    path('map/',                 location_map,      name='owner-map'),
    path('landing/',             intro,             name='Landing-Page'),
    path('login/',               sign_in,           name='Login'),
    path('signup/',              sign_up,           name='SignUp'),
    path('image-slide/',         image_post,        name='Slides'),
    path('vid/',                 video_post,        name='videos'),
]

