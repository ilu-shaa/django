from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import views
from . import converters 



register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'), #main
    path('about/', views.about, name='about'), 
    path('cats/<int:cat_id>/', views.categori, name='cat_id'), #slug все стмволы
    path('cats/<slug:cat_slug>/', views.categori_by_slug,name='cat_slug'), #slug все стмволы
    path("archive/<year4:year>/", views.arch, name='archive'), #slug все стмволы
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
