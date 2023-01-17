from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('message.urls', namespace='message')),
    # path('', include('message.urls', namespace='message')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
]
