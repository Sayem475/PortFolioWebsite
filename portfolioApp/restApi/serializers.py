from portfolioApp.models import Skills
from rest_framework import serializers

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['id','skill']