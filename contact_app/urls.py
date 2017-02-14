from django.conf.urls import url
from .views import ContactListView, ContactDetail


urlpatterns = [
    url(r'^api/v1/contact/$', ContactListView.as_view()),
    url(r'^api/v1/contact/(?P<id>[0-9]+)$', ContactDetail.as_view()),

]
