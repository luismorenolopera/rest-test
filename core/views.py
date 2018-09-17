from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Mentor
from core.serializers import MentorSerializer

# Create your views here.

@api_view()
def users(request):
    query = Mentor.objects.all()
    serializer = MentorSerializer(query, many=True)
    return Response(serializer.data)
