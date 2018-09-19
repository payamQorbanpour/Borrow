from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

from .forms import LoginForm

urlpatterns = [

    url(r'^login/$', auth_views.login, {'authentication_form':LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # change password urls
    url(r'^dashboard/password-change/$', auth_views.password_change, name='change_password'),
    url(r'^dashboard/password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    ]
