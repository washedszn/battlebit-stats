from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/battlebit/', include('battlebit.urls')),  # includes the URLs of the 'battlebit' app
]