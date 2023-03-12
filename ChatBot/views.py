from django.http import HttpResponse  # used to give response to browser(text based)
from django.shortcuts import render
from django.http import JsonResponse
import json


def heropage(request):
    #return render(request,"index.html")
    return render(request,"Hero.html")

def chatpage(request):
    return render(request,"Chat.html")
    

def buttonmsg(request,buttonName):
    with open('static/javascript/keyword.json','r') as f:
        data = json.load(f)
    mylist=[]
    for i in data[buttonName]:
        mylist.append(i)
    mylist.append(buttonName)
    mylist_json = json.dumps(mylist)
    return JsonResponse({'mylist':mylist_json})
     
def subbuttonmsg(request,corekey,content):
    with open('static/javascript/keyword.json','r') as f:
        data = json.load(f) 
    subbuttonresponse=data[corekey][content]
    ans=json.dumps(subbuttonresponse)
    return JsonResponse({'subbuttonresponse':ans})