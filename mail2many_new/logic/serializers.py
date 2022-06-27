from rest_framework import serializers
from .models import EmailListUpload, EmailReceipientRelationship

class EmailListUploadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmailListUpload
        fields = ['mail_title', 'mail_text', 'upload_description', 'timestamp', 'spreadsheet', 'author', 'sender_email']
    

class EmailReceipientRelationshipSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmailReceipientRelationship
        fields = ['email_upload_list', 'recipient_name', 'reciever_email', 'intended_message']
        
    