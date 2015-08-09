from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.twiml import Response
from django_twilio.decorators import twilio_view

# Create your views here.
@twilio_view
def reply_to_sms_messages(request):
    r = Response()
    r.sms('Thanks for the SMS message!')
    return r





# @csrf_exempt
# def sms(request):
    # twiml = '<Response><Message>Hello from your Django app!</Message></Response>'
    # return HttpResponse(twiml, content_type='text/xml')
