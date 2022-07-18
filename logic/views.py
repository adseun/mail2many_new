import email
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
import csv

from logic.emails import send_email

from .serializers import EmailListUploadSerializer, EmailReceipientRelationshipSerializer
from .models import EmailListUpload, EmailReceipientRelationship
from rest_framework.permissions import AllowAny



from rest_framework import status
class SendEmailAPIView(APIView):
    permission_classes=(AllowAny,)
    
    def post(self,request,*args,**kwargs):
        serializer = EmailListUploadSerializer(data=request.data)
        # file_type=request.data["file_type"]
        file_type= "https://res.cloudinary.com/mail2many/raw/upload/v1657322583/ABAJI_bms6aw.xlsx"
        if file_type != "xlsx" or file_type != "csv":
            return Response(data={"message":"File type unacceptable"}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            spreadsheet=request.data["spreadsheet"]
            if file_type == "xlsx":
                pass
            elif file_type == "csv":
                with open(spreadsheet, 'r') as file:
                    csvreader = csv.reader(file)
                    names = []
                    emails = []
                    row_count = 0
                    for row in csvreader:  
                        if row_count == 0:
                            row_count += 1
                        else:        
                            names.append(row[1])
                            emails.append(row[0])
                            row_count +=1
                    send_mail=send_email(emails, names) 
                    
                return Response(data={"message":"Excel Uploaded successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
                        
            else:
                return Response(data={"message":"File type unacceptable"}, status=status.HTTP_403_FORBIDDEN)

        else:
            print(serializer.errors)
            return Response(data={"message":serializer.errors})
        
        
        
        
        # send_email_function = self.send_email_function
        # return Response(data={"message":"Category created"}, status=status.HTTP_201_CREATED)
    
    def send_email_function(self):       
        df = pd.read_csv('https://res.cloudinary.com/mail2many/raw/upload/v1657322583/ABAJI_bms6aw.xlsx')
        name = df['name'].values
        email = df['email'].values
    
    
    def get(self, request, *args, **kwargs):
        emails = EmailListUpload.objects.all()
        serializer = EmailListUploadSerializer(emails, many=True)
        return Response(serializer.data)
    
class SendEmailDetailView(APIView):
    
    def get(self, request, id, *args, **kwargs):
        try:
            email= EmailListUpload.objects.get(id=id)
        except EmailListUpload.DoesNotExist:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = EmailListUploadSerializer(email)
        return Response(serializer.data)
    
    
    def put(self, request, id, *args, **kwargs):
        email= EmailListUpload.objects.get(id=id)
        serializer = EmailListUploadSerializer(email)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id, *args, **kwargs):
        email = EmailListUpload.objects.get(id=id)
        email.delete()
        return Response(status =status.HTTP_404_NOT_FOUND)
        
        
        
# {
#         "mail_title": "Mail to fuad",
#         "mail_text": "Dear Fuad, Lorem blah blah blah",
#         "upload_description": "Ikorodu spreadsheet",
#          "sender_email": "adeshinafuad@gmail.com"
#     }
        