from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header="Login to Developer Aditya"
admin.site.site_title="Welcome to Aditya's Dashboard"

urlpatterns = [
    path('', views.home, name="home"),
    path('about',views.about,name="about"),
 path('project',views.projects,name="projects"),
     path('contact',views.contact,name="contact"),
]


# [
#     path('', views.home,name="home"),
#     path('about',views.about,name="about"),
#     path('project',views.proje cts,name="projects"),
#     path('contact',views.contact,name="contact")
# ]