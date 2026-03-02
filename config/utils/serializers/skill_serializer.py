from rest_framework import serializers


LEVEL_TEXT = {
    1: "Beginner",
    2: "Intermediate",
    3: "Advanced",
    4: "Expert",
    5: "Master",
}

CATEGORY_TEXT = {
    1: "Frontend",
    2: "Backend",
    3: "DevOps - Cloud & Deployment",
    4: "Databases",
    5: "Blockchain & Web3",
    6: "Programming Languages"
}

class SkillSerializer(serializers.Serializer):
    LEVEL_CHOICES = [(1, "Begginer"), (2, "Intermediate"), (3, "Advanced")]
    name = serializers.CharField()
    level = serializers.SerializerMethodField()
    code = serializers.IntegerField()

    def get_level(self, obj):
        return LEVEL_TEXT.get(obj.level, "Unknown")