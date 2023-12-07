from django.contrib import admin
from django.urls import path

admin.site.site_header = 'TSUE DBMWORK'
admin.site.index_title = 'CONFIGURATIONS'

urlpatterns = [
    path('admin/', admin.site.urls),
]
