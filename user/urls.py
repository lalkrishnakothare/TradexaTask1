from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('myposts/', views.myposts, name='myposts'),
    path('createpost/', views.create_post, name='createpost'),
]