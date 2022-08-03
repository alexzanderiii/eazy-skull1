from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.index, name='index'),

    path("clearance", views.clearance, name='clearance'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),  
    path("work", views.work, name='work'), 
    path("registration", views.registration, name='registration'),
    path("exam", views.exam, name='exam'),
    path("project", views.project, name='project'),      
    path("form_group", views.form_group, name='form_group'),     
    path("form_individual", views.form_individual, name='form_individual'), 
    path("howto", views.howto, name='howto'),     
    path("orientation", views.orientation, name='orientation'),  
    path("profile", views.profile, name='profile'),  
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name='signup'),
    path("OT_search", views.OT_search, name='OT_search'),  
    path("account", views.account, name='account'),  
    path("account_settings", views.account_settings, name='account_settings'),            
]