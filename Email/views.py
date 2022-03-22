from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import EmailMessage,EmailMultiAlternatives
from smtplib import SMTPAuthenticationError
from django.template.loader import render_to_string
# Create your views here.



class SendEmailView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):

        username = request.data['username']
        send_to = request.data['send_to']
        
        htmly_content = render_to_string("Email/email_template.html",{"username":username})
        
        subject =  "BooksApp Welcomes You {}".format(username)
        from_email = 'ritik.artwrk@gmail.com'
        try:
            msg = EmailMultiAlternatives(subject,"",from_email,[send_to])
            msg.attach_alternative(htmly_content,"text/html")
            msg.send()
            return Response({'message':'Email Sent Successfully'})
        except SMTPAuthenticationError:
            return Response({'message':'Something Went Wrong'})