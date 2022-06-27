
from django.urls import path
from .views import HomeApiView


app_name = 'logic'
urlpatterns = [
    # path('', admin.site.urls),
    path('',HomeApiView.as_view(), name='home')
]
