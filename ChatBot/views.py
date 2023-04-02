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

def majorKeywordRetrival(request):
    with open('static/javascript/keyword.json','r') as f:
        data = json.load(f)
    MajorKeyword=[]
    for i in data:
        MajorKeyword.append(i)
    MajorKeyword_json = json.dumps(MajorKeyword)
    return JsonResponse({'MajorKeyword':MajorKeyword_json})
    

     
def subbuttonmsg(request,corekey,content):
    with open('static/javascript/keyword.json','r') as f:
        data = json.load(f) 
    subbuttonresponse=data[corekey][content]
    ans=json.dumps(subbuttonresponse)
    return JsonResponse({'subbuttonresponse':ans})


def adminpage(request):
    return render(request,"adminHeader.html")

def add(request):
    return render(request,"add.html")

def updateAnswer(request):
    return render(request,"updateAnswer.html")

def delete(request):
    return render(request,"delete.html")

def updateKeyword(request):
    return render(request,"updateKeyword.html")


def keywordMsg(request,selectedValue):
    i = 1
    with open('static/javascript/keyword.json','r') as f:
        data = json.load(f) 
    KeywordResponseList=[]
    for key, value in data[selectedValue].items():
        
        a= str(i)+ ")" + key + " : "+value + "\n"
        KeywordResponseList.append(a)
        i += 1
    KeywordResponseList_json = json.dumps(KeywordResponseList)
    return JsonResponse({'KeywordResponseList':KeywordResponseList_json})

def addElement(request,subKeyVal,inputField,textField):
    with open('static/javascript/keyword.json','r')as f:
        data=json.load(f)
    flag = 0 
    if subKeyVal in data:
        if inputField in data[subKeyVal]:
            a="Error: Subkeyword already exists."
            flag = 1
            return JsonResponse({"success": False, "message": "Subkeyword already exists."})
        else:
            data[subKeyVal][inputField] = textField
            a="Added successfully"
            flag = 2
            return JsonResponse({"success": True, "message": "Subkeyword added successfully."})
    else:
        data[subKeyVal] = {inputField: textField}
        with open('static/javascript/keyword.json', 'w') as f:
            json.dump(data, f)
        a="Added successfully"
        flag = 2
        return JsonResponse({"success": True, "message": "Subkeyword added successfully."})

        

        

def deleteElement(request,subKeyVal,inputField):
    
    with open('static/javascript/keyword.json','r')as f:
        data=json.load(f)

    del data[subKeyVal][inputField]

    with open('static/javascript/keyword.json', 'w') as f:
        json.dump(data, f)
    
    return JsonResponse({"message": "keyword deleted successfully."})


def keyupdate(request, subKeyVal, inputField, updatedKey):
    with open('static/javascript/keyword.json','r')as f:
        data=json.load(f)

    data[subKeyVal][updatedKey]=data[subKeyVal][inputField]
    del data[subKeyVal][inputField]

    with open('static/javascript/keyword.json', 'w') as f:
        json.dump(data, f)
    return JsonResponse({"message": "keyword updated successfully."})

def ansupdate(request,subKeyVal, inputField, updatedAnswer):
    with open('static/javascript/keyword.json','r')as f:
        data=json.load(f)

    data[subKeyVal][inputField]=updatedAnswer
    print(data[subKeyVal][inputField])

    with open('static/javascript/keyword.json', 'w') as f:
        json.dump(data, f)
    return JsonResponse({"message": "Answer updated successfully."})
