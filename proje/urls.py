from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('aliwko1999999/', admin.site.urls),
    path('',include("pages.urls")),

] 
handler404 = "pages.views.error404" 
handler500 = "pages.views.error500" 
