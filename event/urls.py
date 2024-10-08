from django.urls import path
from . import views


app_name = 'event'

urlpatterns = [
    path('event/', views.event_details, name='event'),
    path('event_registration/', views.event_registration, name='event_registration'),
    path('event_submit/', views.event_form_submit, name='event_submit'),
    path('eventsubmit_form/', views.submited_form, name='eventsubmit_form'),
    path('event_details/', views.event_details, name='event_details'),
    path('specific_event_details/<str:event_name>',views.specific_event_details, name='specific_event_details'),
    path('event_image/<int:id>', views.event_image, name='event_image'),
    path('event_all_image/', views.event_all_images, name='event_all_image'),
]  


