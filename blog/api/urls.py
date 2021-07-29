from django.urls import path
from .views import ApiForAllCommentsView

urlpatterns = [
     path('comments/', ApiForAllCommentsView.as_view(), name='all-comments-api'),
]

