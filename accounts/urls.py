from django.urls import path, include

app_name = 'account'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]
