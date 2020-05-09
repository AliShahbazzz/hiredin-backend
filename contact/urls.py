from django.urls import path
from .import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.ContactUsAPIView.as_view(), name='contact'),
    
]