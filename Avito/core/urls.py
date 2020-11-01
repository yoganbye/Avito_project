from django.contrib import admin
from django.urls import path, include, reverse_lazy
from . import views, auth_views
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, 
    PasswordResetConfirmView, PasswordResetCompleteView
)


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('announcement/', views.announce, name='announce'),

    path('announcement/<int:announce_id>/', views.AnnounceView.as_view(), name='det_announce'),

    path('announcement/create/', views.CreateAdView.as_view(), name='ad_create'),

    path('announcement/<int:announce_id>/edit/', views.EditeAdView.as_view(), name='ad_edit'),
    
    path('announcement/<int:announce_id>/delete/', views.DeleteAdView.as_view(), name='ad_delete'),

    path('categories/', views.categories, name='categories'),

    path('categories/<int:categories_id>/', views.det_categories, name='det_categories'),

    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('registration/', auth_views.SignupView.as_view(), name='signup'),

    path('logout/', auth_views.logout_view, name='logout'),

    path('profile/<int:user_id>/', auth_views.ProfileView.as_view(), name='profile'),

    path('password_reset/', PasswordResetView.as_view(
        success_url=reverse_lazy('password_reset_done'),
        template_name='my_auth/password_reset.html'
    ), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='my_auth/password_reset_done.html'
    ), name='password_reset_done'),

    path('password_reset/<str:uidb64>/<slug:token>', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),

    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]