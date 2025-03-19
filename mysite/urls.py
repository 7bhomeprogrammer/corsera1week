from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls', namespace='polls')),
    path('admin/', admin.site.urls),

]
