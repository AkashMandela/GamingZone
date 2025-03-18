
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Akash Admin"
admin.site.site_title = "Gaming zone"
admin.site.index_title = "Welcome to Gaming zone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about', include('home.urls')),
    
]

