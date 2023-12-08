from django.urls import path, include

from .views import main, sync_losses_list

urlpatterns = [
    path('', main, name='losses'),
    path('sync/', sync_losses_list, name='losses_sync'),
]
