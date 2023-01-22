from django.urls import path
from .views import IndexView, Error404View, Error500View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('404/', Error404View.as_view(), name='error404'),
    path('500/', Error500View.as_view(), name='error500'),
]
