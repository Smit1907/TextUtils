#i have created this website
from ast import Param
from distutils.command.bdist import show_formats
from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render

# # Code For Video 6
# def index(request):
#     return HttpResponse('''<h1>Index</h1> <a href = "https://www.facebook.com/login/">FaceBook</a> <br> <a href = "https://www.geeksforgeeks.org/">geeksforgeeks</a> <br> <a href = "https://www.logixbuilt.com/">logixbuilt</a> <br> <a href = "https://www.youtube.com/">youtube</a> <br> <a href = "https://www.instagram.com/">instagram</a>''')

# def about(request):
#     return HttpResponse("about hello")

def index(request):
    # return HttpResponse('''<h1><a href = "/">Home</a></h1> ''')
    return render(request, 'index2.html') 

def analyze(request):
    # get the text
    djtext= request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','default')
    fullcaps= request.POST.get('fullcaps','default')
    newlineremover = request.POST.get('newlineremover','default')
    spaceremover = request.POST.get('spaceremover','default')
    charcount = request.POST.get('charcount','default')
    # analyzed = ""
    show_output = ""
    params = {}
    # djtext= request.GET.get('text','default')
    # removepunc= request.GET.get('removepunc','default')
    # fullcaps= request.GET.get('fullcaps','default')
    # newlineremover = request.GET.get('newlineremover','default')
    # spaceremover = request.GET.get('spaceremover','default')
    # charcount = request.GET.get('charcount','default')
    
    # analyzed = djtext
    #'removed Punction'
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'removed Punction', 'analyzed_text': analyzed}
        # show_output = analyzed #+ "removed Punction"
        
        # analizing text
        # return HttpResponse("remove punc <a href ='/'>back</a>")
        # return render(request, 'analyze.html',params)

    #Changed to UPPERCASE
    if fullcaps == "on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper() 
        params = {'purpose':'Changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext =  analyzed #+ "Changed to UPPERCASE"
        # return render(request, 'analyze.html',params)
        
    #new line remove
    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose':'new line removed', 'analyzed_text': analyzed}
        djtext =  analyzed #+ "new line remove"
        # return render(request, 'analyze.html',params)
        
    #space remove
    if spaceremover == "on":
        analyzed=" "
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose':'Space remove', 'analyzed_text': analyzed}
        djtext =  analyzed #+ "space remove"
        # return render(request, 'analyze.html',params)

    #character count
    if charcount == "on":
        
        count=0
        for i in djtext:
            if i == " " or i == "\n":
                pass
            else:
                count+=1
        analyzed1=f"\ntotal number are : {count}"    
        show_output  =  str(analyzed) + str(analyzed1)
        params = {'purpose':'character count', 'analyzed_text': show_output}
        
        
        #return render(request, 'analyze.html',params1)

    # else:
    #     return HttpResponse("error")
    if(removepunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")
    
    return render(request, 'analyze2.html',params)

    
          
    

























# def capfirst(request):
#     return HttpResponse("Capitalize first <a href ='/'>back</a>") 

# def newlineremove(request):
#     return HttpResponse("newline remove <a href ='/'>back</a>") 

# def spaceremove(request):
#     return HttpResponse("space remove <a href ='/'>back</a>") 

# def charcount(request):
#     return HttpResponse("char count <a href ='/'>back</a>") 