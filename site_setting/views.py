from django.shortcuts import render
from .serializers import SiteSocialMediaSerializer
from .models import SiteSettings

# rest framework 
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
# @permission_classes([AllowAny])
def view_siteSettings(request):
        
    if request.method == 'GET':
        q_Settings = SiteSettings.objects.all()
        print(q_Settings)
        serializer = SiteSocialMediaSerializer(q_Settings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message":"درخواست نامعتبر است"}, status=status.HTTP_400_BAD_REQUEST)
