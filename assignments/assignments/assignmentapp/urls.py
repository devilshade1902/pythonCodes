from django.urls import path
from .views import PostCreateView,PostUpdateView,PostDeleteView
from .views import PostListView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/list/', PostListView.as_view(), name='post_list'),
     path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
     path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete')
]
