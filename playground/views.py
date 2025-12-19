from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
import requests
import logging

logger = logging.getLogger(__name__)



class HelloView(APIView):
  def get(self,request):
    try:
      logger.info('calling httpbin')
      response = requests.get('https://httpbin.org/delay/2')
      data = response.json() 
    except requests.ConnectionError:
      logger.critical('httpbin is down') 
    return render(request, 'hello.html', {'name': 'Anshik'})
    





# def say_hello(request):
#     try:
#        message = BaseEmailMessage(
#            template_name='emails/hello.html',
#            context={
#                'name': 'Anshik'
#            }
#        )
#        message.send(['anshik@mo.com'])
#     except BadHeaderError:    
#         pass
#     return render(request, 'hello.html', {'name': 'Mosh'})
