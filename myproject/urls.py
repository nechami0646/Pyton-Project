from django.contrib import admin
from django.urls import path, include # הוסיפי את include כאן

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')), # הפניה לקובץ ה-urls הפנימי
]