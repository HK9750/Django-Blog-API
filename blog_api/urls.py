from django.urls import path
from .views import ListPosts, EditPost, DeletePost, SearchPost, PostDetail

urlpatterns = [
    path('', ListPosts.as_view(), name='listcreate'),
    path('editpost/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('deletepost/<int:pk>/', DeletePost.as_view(), name='deletepost'),
    path('searchpost/', SearchPost.as_view(), name='searchpost'),
    path('postdetail/<str:pk>/', PostDetail.as_view(), name='postdetail')
]
