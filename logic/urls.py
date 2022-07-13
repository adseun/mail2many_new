
from django.urls import path
from .views import SendEmailAPIView,SendEmailDetailView


app_name = 'logic'
urlpatterns = [
    path('send-email',SendEmailAPIView.as_view(), name='home'),
    path('send-email/details/<str:id>', SendEmailDetailView.as_view(), name='home'),   
]
