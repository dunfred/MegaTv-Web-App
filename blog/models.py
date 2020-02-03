from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$', message="Enter your phone here.")

class BlogUser(AbstractUser):
    first_name   = models.CharField(default="" ,null=False, blank=False, max_length=120, unique=True)
    last_name    = models.CharField(default="" ,null=False, blank=False, max_length=120, unique=True)
    username     = models.CharField(default="" ,null=False, blank=False, max_length=120, unique=True)
    email        = models.EmailField(default="" ,null=False, blank=False)    
    password     = models.CharField(default="", null=False, blank=False, max_length=150)
    phone_number = models.CharField(default="" ,validators=[phone_regex], max_length=17, blank=False)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):    
    post_title = models.CharField(default="Post Title",max_length=50)
    post_brief = models.CharField(default="Post Brief",max_length=150)
    post_thumbnail = models.ImageField(blank=True, upload_to='blog/thumbs/%Y/%B/%a/')
    post_content = models.TextField()    
    post_images = models.ImageField(blank=True, upload_to='blog/images/%Y/%B/%a/')    
    post_videos = models.FileField(blank=True, upload_to='blog/videos/%Y/%B/%a/')
    created_on = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)
    category = models.ManyToManyField("Category",related_name='posts')
    slug = models.SlugField(null=True, unique=True)
    #user = models.ForeignKey('BlogUser', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.post_title)
        super(Post, self).save(*args, **kwargs)
  
    def __str__(self):
        return self.post_title

class PostImage(models.Model):
    post_images = models.ImageField(blank=True, upload_to='blog/images/%Y/%B/%a/')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.post_title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
