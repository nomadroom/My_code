from django.urls import path, re_path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.login, name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
    re_path(r'^create/$', authapp.create, name='create'),
    re_path(r'^edit/$', authapp.edit, name='edit'),
    re_path(r'verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),

]
