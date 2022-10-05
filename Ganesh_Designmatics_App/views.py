from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RegisterCompany(APIView):
    def post(self, request):
        params = request.POST.dict()
        serializer = LogoSerializer(data=params)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SUCCESS', 'status': status.HTTP_201_CREATED, 'result': 'Company Registered Successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'FAILED', 'status': status.HTTP_400_BAD_REQUEST, 'result': serializer.errors}, status=status.HTTP_200_OK)

class GetLogosView(APIView):
    def post(self, request):
        params = request.POST.dict()
        try:
            company_name = params['company_name']
            comp = Logo.objects.get(company_name=company_name)
            if comp is not None:
                return Response({'message': 'SUCCESS', 'status': status.HTTP_200_OK, 'result': str(comp.company_name)}, status=status.HTTP_200_OK)
            return Response({'message': 'FAILED', 'status': status.HTTP_400_BAD_REQUEST, 'result': 'Company Not Found'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'FAILED', 'status': status.HTTP_400_BAD_REQUEST, 'result': 'PlEASE CHECK YOUR PARAMETERS!'}, status=status.HTTP_200_OK)