from django.urls import path
from . import views
app_name = 'app_name'
urlpatterns = [
#    path('top_page/', views.top_page, name='top_page'),
    path('uploadview/', views.uploadview, name='uploadview') 
]