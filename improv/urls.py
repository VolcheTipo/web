from django.urls import path, include
from . import views
from .views import SignUpView , logout_view
from django.conf import settings
import django.conf.urls.static  
from .views import CreateProfilePageView

urlpatterns = [
    path('home/', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('auto/', views.LeadListCreate.as_view()),
    path('login/',views.user_login, name='login'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name='create_user_profile'),
    path('profile/',views.user_profile,name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('svyaz/', views.svyaz, name = 'svyaz'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
