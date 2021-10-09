#i have created this file
from django.http import HttpResponse

from django.shortcuts import render



def index(request):


    return render(request,'index.html')

def analyze(request):

   #Get the text

   djtext = request.GET.get('text', 'default')
   removepunc = request.GET.get('removepunc', 'off')
   Upper = request.GET.get('Upper', 'off')
   Charco=request.GET.get('Charc', 'off')
   #print(djtext)
  # print(removepunc)
   if (removepunc=="on"):
       punctuations=''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

       analyzed=""

       for char in djtext:
           if char not in punctuations:
               analyzed=analyzed+char
       params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
       return render(request,'analyze.html',params)
   elif(Upper=="on"):
       analyzed=""
       for char in djtext:
           analyzed=analyzed+char.upper()

       params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
       return render(request,'analyze.html',params)
   elif(Charco=="on"):
       analyzed=0
       for char in djtext:
           if(char!=' '):
               analyzed = analyzed + 1

       params = {'purpose': 'Total Characters', 'analyzed_text': analyzed}
       return render(request, 'analyze.html', params)

   else:
       return HttpResponse("error")

