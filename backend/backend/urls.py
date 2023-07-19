from django.urls import path, include

urlpatterns = [
    path('', include('battlebit.urls')),  # includes the URLs of the 'battlebit' app
]