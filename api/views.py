from .email import send_message_email
from django.core import serializers
from rest_framework.response import Response
from .serializers import NewsLetterRecipientSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from.models import NewsLetterRecipient
from django.views.generic.list import ListView
from django.views.generic import CreateView
from .forms import NewsLetterForm


@api_view(['GET', 'POST'])
def Recipients(request):
    if request.method == 'GET':
        recipients = NewsLetterRecipient.objects.all()
        serializer = NewsLetterRecipientSerializer(recipients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsLetterRecipientSerializer(data=request.data)
        if serializer.is_valid():
            recipient = NewsLetterRecipient(
                email=serializer.data['email']
            )
            recipient.save()
            send_message_email(recipient.email, recipient.email)

            return Response(
                {
                    "success": True,
                    "message": "Email was sent successfully",
                    "data": {
                        "email": serializer.data['email'],
                        "date_registered": recipient.date_registered,
                    }
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

class NewsletterRecipientsListView(ListView):
    
    model = NewsLetterRecipient
    template_name = 'recipients.html'
    context_object_name = 'recipients'
    ordering = ['-date_registered']
    paginate_by = 4
    

class NewsletterRecipientCreateView(CreateView):
    
    model = NewsLetterRecipient
    fields = ['email']
    template_name = 'newsletterrecipient_form.html'
    
    
