from django.urls import path

from . import views

app_name = 'offers'

urlpatterns = [
    path('categories', views.get_categories, name='get_categories'),
    path('localizations', views.get_localizations, name='get_localizations'),
    path('conditions', views.get_conditions, name='get_conditions'),
    path('delete/<int:offer_id>', views.delete_offer, name='delete_offer'),
    path('<int:offer_id>', views.get_offer, name='detail_offer'),
]
