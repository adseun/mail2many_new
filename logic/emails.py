from django.core.mail import send_mass_mail
import pandas as pd

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
def read_csv(csv_link):
    df = pd.read_csv('namesandemails.csv')
    names = df.loc[:, 'name'].to_list()
    emails = df.loc[:, 'email'].to_list()
    messages = df.loc[:, 'message'].to_list()
    return names, emails
    
        