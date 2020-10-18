from django.urls import path
from . import views
 
app_name = 'jobs'
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    # path('import/', views.import_view, name='import'),
    ]