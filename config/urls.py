from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign-up/', include('source.accounts.urls')),
    path('', include('source.main.urls')),

]
