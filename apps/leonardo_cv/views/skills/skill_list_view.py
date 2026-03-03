from rest_framework.views import APIView
from rest_framework.response import Response

from apps.leonardo_cv.domain.skill import Skill
from apps.leonardo_cv.serializers.skill_serializer import SkillSerializer


ALL_SKILLS = [

    # Frontend (1)
    Skill("HTML", 3, "html5", 1),
    Skill("CSS", 3, "css", 1),
    Skill("React", 3, "react", 1),
    Skill("Vue", 3, "vue", 1),
    Skill("Angular", 3, "angular", 1),
    Skill("TailwindCSS", 3, "tailwindcss", 1),
    Skill("Pinia", 3, "pinia", 1),
    Skill("Bootstrap", 3, "bootstrap", 1),
    Skill("Vite", 3, "vite", 1),

    # Backend (2)
    Skill(".NET", 3, "dotnet", 2),
    Skill("ASP.NET Core Web API", 3, "aspnetcore", 2),
    Skill("LINQ", 3, "linq", 2),
    Skill("EF Core", 3, "efcore", 2),
    Skill("AutoMapper", 3, "automapper", 2),
    Skill("JWT Bearer Auth", 3, "jwtbearer", 2),
    Skill("Dependency Injection", 3, "dependencyinjection", 2),
    Skill("SwaggerUI", 3, "swagger", 2),
    Skill("NestJS", 3, "nestjs", 2),
    Skill("Prisma ORM", 3, "prisma", 2),

    # DevOps - Cloud & Deployment (3)
    Skill("Docker", 3, "docker", 3),
    Skill("Linux Servers", 3, "linux", 3),
    Skill("AWS - EC2 Instances", 3, "awsec2", 3),
    Skill("Git", 3, "git", 3),

    # Databases (4)
    Skill("MySQL", 3, "mysql", 4),
    Skill("PostgreSQL", 3, "postgresql", 4),
    Skill("SQL Server", 3, "sqlserver", 4),

    # Blockchain & Web3 (5)
    Skill("Hyperledger Besu", 3, "hyperledgerbesu", 5),
    Skill("Solidity", 3, "solidity", 5),
    Skill("Ethers.js", 3, "etherjs", 5),

    # Programming Languages (6)
    Skill("C#", 3, "csharp", 6),
    Skill("Typescript", 3, "typescript", 6),
    Skill("Javascript", 3, "javascript", 6),
    Skill("Python", 3, "python", 6),
    Skill("C++", 3, "cpp", 6),
]


class SkillListView(APIView):
    def get(self, request):

        skill_type_param = request.query_params.get('skill_type')

        res = ALL_SKILLS

        for i in res:
            print(f"{i.name}, {i.skill_type}") 
        
        if skill_type_param:
            skill_type = int(request.query_params.get('skill_type'))
            res = list(filter((lambda s: s.skill_type == skill_type), ALL_SKILLS))

        serializer = SkillSerializer(res, many=True)
        return Response(serializer.data)
