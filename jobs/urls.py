from django.urls import path
from . import views
 
app_name = 'jobs'
 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('apply/<int:job_id>/', views.apply, name='apply'),
    # path('import/', views.import_view, name='import'),
    ]