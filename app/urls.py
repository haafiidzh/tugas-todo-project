
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # add route from todo Application
    path('todo/', include('todo.urls'))
]