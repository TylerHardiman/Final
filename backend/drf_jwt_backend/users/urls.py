from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_abuse_log),
    path('user/posts/', views.user_abuse_log),
    path('user/comments/', views.user_comments),
    path('user/editabuselog/<int:pk>/', views.edit_abuse_log),
    path('user/editcomment/<int:pk>/', views.edit_comment),
    path('comments/', views.get_all_comments),
    path('user/deletecomment/<int:pk>/', views.delete_comment),
    
]
