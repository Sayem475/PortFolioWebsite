# $$$$$$$$$$$  WE CAN SIMPLY USE THIS VIEWSETS METHOD INSTEAD OF APIVIEW     $$$$$$$

from django.shortcuts import render 
from portfolioApp.models import Skills
from rest_framework import permissions
from rest_framework import viewsets

from portfolioApp.restApi.serializers import SkillsSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


# from portfolioApp.models import Skills
# from portfolioApp.restApi.serializers import SkillsSerializer

# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class SkillsList(APIView):
#     def get(self, request, format=None):
#         skill = Skills.objects.all()
#         serializer = SkillsSerializer(skill, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer =  SkillsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SkillsDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Skills.objects.get(pk=pk)
#         except Skills.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         skill = self.get_object(pk)
#         serializer = SkillsSerializer(skill)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         skill = self.get_object(pk)
#         serializer = SkillsSerializer(skill, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         skill = self.get_object(pk)
#         skill.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


