from django.urls import path, include
from . import views
from rest_framework import routers
from . import views


urlpatterns = [
  path('newsletter_recipients1/', views.Recipients, name='recipients'),
  path('newsletter_recipients2/', views.NewsletterRecipientsListView.as_view(), name='recipients2')
]