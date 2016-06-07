from register.models import *
from django.conf.urls import url
from django.views.generic import TemplateView
from register.views import *

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='login'),
    url(r'^user/success/', TemplateView.as_view(template_name='registration/user/success.html'),
        name='user_registration_success'),
    url(r'^chocolate/add/', AddChocolateview.as_view(), name='add_chocolate'),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info")
]
