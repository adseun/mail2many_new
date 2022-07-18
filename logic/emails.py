from django.core.mail import send_mass_mail

def send_email(emails, names):
    sender_email = "mail2many@gmail.com"
    # for email, email in zip(emails, names):
        
    send_mass_mail(
        'subject',
        'message',
        sender_email,
        emails, fail_silently=False
    )
    
    return True
    
        