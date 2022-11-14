from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about, name='about-us'),
    path('skin-type/', views.skintype, name='skin-type'),
    path('acne-test/', views.acnetest, name='acne-test'),
    path('nail-test/', views.nailtest, name='nail-test'),
    path('use/', views.use, name='use'),
    # path('real-time/', views.index, name='real-time'),
    # path('real-time/camera_feed', views.camera_feed, name='camera_feed'),
]
