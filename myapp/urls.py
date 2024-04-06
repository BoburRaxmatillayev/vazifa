from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="hello"),
    path('about/',views.main1,name="hello"),
    path('uy/',views.main2,name="hello"),
    path('main/',views.main4,name="hello"),
]
