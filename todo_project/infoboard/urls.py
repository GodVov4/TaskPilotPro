from django.urls import path, include

from .views import main, sync_losses_list

urlpatterns = [
    path('', main, name='main'),
    path('sync/', sync_losses_list, name='losses_sync'),
]
