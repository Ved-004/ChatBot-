from django.http import HttpResponse  # used to give response to browser(text based)
from django.shortcuts import render
from django.http import JsonResponse
import json


def heropage(request):
    #return render(request,"index.html")
    return render(request,"Hero.html")

def chatpage(request):
    return render(request,"Chat.html")
    

def buttonmsg(request,button_id):
    with open('static\keyword.json','r') as f:
        data = json.load(f)
    mylist=[]
    for i in data[button_id]:
        mylist.append(i)
        #list.append('\n')
        mylist_json = json.dumps(mylist)
    return JsonResponse({'mylist':mylist_json})
        