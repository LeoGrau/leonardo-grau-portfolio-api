from rest_framework.views import APIView
from rest_framework.response import Response

from config.domain.skill import Skill
from config.utils.serializers.skill_serializer import SkillSerializer


class SkillView(APIView):
    def get(self, request):
        skills = [
            Skill(".NET", 2, 1),
            Skill("React", 2, 2),
            Skill("Python", 2, 3)
        ]
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
