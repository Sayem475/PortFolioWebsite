from django.urls import path, include
from . import views
from django.views import View
from .views import Home,Details


urlpatterns = [
    path('', Home.as_view()),
    path('<int:id>/', Details.as_view(), name="ports"),
    path('api/', include('portfolioApp.restApi.urls')),
]
