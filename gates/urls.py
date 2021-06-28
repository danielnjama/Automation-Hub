from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
path('',views.home, name='home'),
path('contact-us/',views.contact,name='contact'),
path('send_email/',views.send_email,name='send_email'),
path('swinging-gates/',views.swinging_gates, name='swinging_gates'),
path('sliding-gates/',views.sliding_gates, name='sliding_gates'),
path('garage-gates/',views.garage_gates, name='garage_gates'),
path('about-us/',views.aboutus,name='aboutus'),
path('cctvs&floodlights/',views.cctv,name='cctv'),
path('tarragon-gallery/',views.gallery,name='gallery'),

]

urlpatterns += [
    url(r'^(?P<types>[\w-]+)/(?P<slug>[\w-]+)/$',views.item_detail,name='item_detail'),
]
