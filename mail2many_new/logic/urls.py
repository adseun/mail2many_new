
from django.urls import path
from .views import SendEmailAPIView


app_name = 'logic'
urlpatterns = [
    # path('', admin.site.urls),
    path('send-email',SendEmailAPIView.as_view(), name='home'),
]
