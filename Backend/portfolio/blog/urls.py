from django.urls import path
from . import views
from .views import contact_view
urlpatterns = [
    path('contact/', views.contact, name='contact'),
     path('contact/', contact_view, name='contact'),  # Contact form
    path('contact/success/', lambda request: render(request, 'contact_success.html'), name='contact_success'),  # Success page
]
