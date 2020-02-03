from django.urls import path
from .views import CommentListView, ApiForAllCommentsView, ApiForPostCommentsView

urlpatterns = [
     path('', ApiForAllCommentsView.as_view(), name='test-json-view'),
     path('<int:post>/', ApiForPostCommentsView.as_view(), name='post-json-view'),
     path('comments/', CommentListView.as_view(), name="comment-api-view")
]

