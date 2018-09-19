from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = [

    # User login
    url(r'^login/$', auth_views.login, {'authentication_form':LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # User registration
    url(r'^register/$', views.register, name='register'),

    # change password urls
    url(r'^dashboard/password-change/$', auth_views.password_change, name='password-change'),
    url(r'^dashboard/password-change/done/$', auth_views.password_change_done, name='password_change_done'),

    # restore password urls
    url(r'^dashboard/password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^dashboard/password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^dashboard/password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^dashboard/password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # User edit profile
    url(r'^dashboard/edit/$', views.edit, name='edit'),


    ]
