from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response

from .serializers import EmailListUploadSerializer, EmailReceipientRelationshipSerializer
from .models import EmailListUpload, EmailReceipientRelationship
from rest_framework.permissions import AllowAny



from rest_framework import status
class SendEmailAPIView(APIView):
    permission_classes=(AllowAny,)
    
    def post(self,request,*args,**kwargs):
        serializer = EmailListUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message":"Excel Uploaded successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
        
        else:
            print(serializer.errors)
            return Response(data={"message":serializer.errors})
        
        
        
        
        # send_email_function = self.send_email_function
        # return Response(data={"message":"Category created"}, status=status.HTTP_201_CREATED)
    
    # def send_email_function(self, ):       
    #     df = pd.read_csv('annual.csv')
    #     name = df['name'].values
    #     email = df['email'].values
    
    
    def get(self, request, *args, **kwargs):
        emails = EmailListUpload.objects.all()
        serializer = EmailListUploadSerializer(emails, many=True)
        return Response(serializer.data)