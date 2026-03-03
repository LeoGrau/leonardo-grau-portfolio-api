from rest_framework import serializers


LEVEL_TEXT = {
    1: "Beginner",
    2: "Intermediate",
    3: "Advanced",
    4: "Expert",
    5: "Master",
}

SKILL_TYPE_TEXT = {
    1: "Frontend",
    2: "Backend",
    3: "DevOps - Cloud & Deployment",
    4: "Databases",
    5: "Blockchain & Web3",
    6: "Programming Languages"
}

class SkillSerializer(serializers.Serializer):
    name = serializers.CharField()
    level = serializers.SerializerMethodField()
    code = serializers.CharField()
    skill_type = serializers.SerializerMethodField()

    def get_level(self, obj):
        return LEVEL_TEXT.get(obj.level, "Unknown")
    
    def get_skill_type(self, obj):
        return SKILL_TYPE_TEXT.get(obj.skill_type, "Unknown")