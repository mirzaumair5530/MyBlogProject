from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('notification/', views.notification, name='notification'),
    path('uploadPost/', views.uploadPost, name='uploadpost'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('post/<str:pk>', views.viewPost, name='viewpost'),
    path('forgotpassword', views.passwordForget, name='passwordForget'),

]