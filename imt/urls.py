from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.index, name='index'),

    path("work-single", views.work_single, name='work-single'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),  
    path("work", views.work, name='work'), 
    path("pricing", views.pricing, name='pricing'),
    path("exam", views.exam, name='exam'),
    path("project", views.project, name='project'),      
     path("form_group", views.form_group, name='form_group'),     
      path("form_individual", views.form_individual, name='form_individual'), 
        path("howto", views.howto, name='howto'),     
       path("orientation", views.orientation, name='orientation'),  
       path("profile", views.profile, name='profile'),            
]