from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('notification/', views.notification, name='notification'),
    path('uploadPost/', views.uploadPost, name='uploadpost'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/<str:pk>', views.viewPost, name='viewpost'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name="passwordForget/passwordForget.html"),
         name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view( ),
         name='password_reset_complete'),

]