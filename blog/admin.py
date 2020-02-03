from django.contrib import admin
from .models import Post, PostImage, Category, Comment, BlogUser

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Post Descriptions",   {"fields": ['post_title','post_brief', 'category']}),
        ("Post Media",          {"fields": ['post_thumbnail','post_images','post_videos']}),
        ("Post Contents",       {"fields": ['post_content']}),
        ("Post Status",         {"fields": ['created_on', 'last_modified']}),
         
    )

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogUser)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
admin.site.register(Comment)
