from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from portfolioApp.restApi import views

router = routers.DefaultRouter()
router.register(r'Skills', views.SkillsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# our portfolioApp API
# http://127.0.0.1:8000/api/



# from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from portfolioApp.restApi import views
# # from portfolioApp.restApi.views import SkillsList, SkillsDetail
# from portfolioApp.restApi.views import SkillsViewSet

# urlpatterns = [
#     path('', include('rest_framework.urls', namespace='rest_framework')),
#     path('skills/', SkillsViewSet.as_view()),
  
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
