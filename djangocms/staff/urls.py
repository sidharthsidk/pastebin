from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='staff_home'),
    path('post/new/',new_post,name='new_post'),
    path('post/delete/<int:id>',post_delete,name='post_delete'),
    path('post/edit/<int:id>',post_edit,name='post_edit')
]