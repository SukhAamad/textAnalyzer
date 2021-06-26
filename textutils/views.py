from django.http import HttpResponse 
from django.shortcuts import render 




def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):


    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps','off')
    extras = request.POST.get('extras', 'off')
    counter = request.POST.get('counter', 'off')
    newlineremover = request.POST.get('lineremover', 'off')




    if removepunc == 'on'  :
        punctuations = '''!()-[]{};:'"\,<>./?@#$%`^*_~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations and extra space', 'analyzed_text': analyzed}  

        djtext = analyzed     
        # return render(request, 'analyze.html', params)




    if (caps == 'on'):

        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char[0].upper()

        params = {'purpose': 'Make UperCases all the way up', 'analyzed_text': analyzed}
        djtext = analyzed     

        # return render(request, 'analyze.html', params)

    
    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        
        djtext=analyzed
        




    
    if extras == 'on':
        

        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
               analyzed = analyzed + char

                
        params = {"purpose": "Remove Extras", 'analyzed_text': analyzed }
        djtext = analyzed    

        # return render(request, 'analyze.html', params)



    if counter == 'on':
        analyzed = 0
        for char in enumerate(djtext):
            analyzed = analyzed + 1

        params = {'purpose': 'Character Count is', 'analyzed_text': analyzed}
        djtext = analyzed   
        
        # return render(request, 'analyze.html', params)
    # if removepunc != 'on' or caps != 'on' or extras != 'on' or counter != 'on':
    #     # return render(request, 'analyze.html', params)
    #     return HttpResponse('Error')

    if(removepunc != "on" and caps !="on" and extras!="on" and counter!="on" and newlineremover !='on'):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)



        

    



    