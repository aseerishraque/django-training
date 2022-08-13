from django.urls import path
from blog.views import post_list, post_details, create_post, update_post

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_details, name='post_details'),
    path('create-post/', create_post, name='create_post'),
    path('update-post/<int:post_id>/', update_post, name='update_post')
    # path('', post_list, name='post_detail'),
]
