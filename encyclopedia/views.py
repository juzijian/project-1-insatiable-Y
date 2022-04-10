import random
import markdown
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    title = request.GET.get("q")
    Entry =util.get_entry(title)
    if Entry == None:
        list=util.part_list_entries(title)
        if list:
         return render(request,"encyclopedia/index.html",{
            "entries":list
        })
        else: 
            return HttpResponseNotFound("Not Found 404")
    else: return render(request, "encyclopedia/display.html", {
        "searchname":title,
        "Entry":markdown.markdown(Entry),
        "Title":title
    })

def random_entry(request):
    list=util.list_entries()
    r = random.randint(0,len(list)-1)
    Entry=util.get_entry(list[r])
    return render(request, "encyclopedia/display.html", {
        "searchname":list[r].title,
        "Entry":markdown.markdown(Entry),
        "Title":list[r].title
    })

def show_entry(request,param):
    title=param
    Entry=util.get_entry(title)
    if Entry==None:
        return HttpResponseNotFound("Not Found 404")
    else: return render(request, "encyclopedia/display.html",{
        "searchname": title,
        "Entry":markdown.markdown(Entry),
        "Title":title
    })

def create_entry(request):
    return render(request,"encyclopedia/creating.html")

def saving_entry(request):
    Title=request.GET.get("t")
    Content=request.GET.get("c")
    Entry=util.get_entry(Title)
    if Entry == None:
     util.save_entry(Title,Content)
     Entry=util.get_entry(Title)
     return render(request, "encyclopedia/display.html",{
        "searchname": Title,
        "Entry": markdown.markdown(Entry)
    })
    else:return HttpResponse("The entry has existed")

def editing_entry(request,param):
    title=param
    Entry=util.get_entry(title)
    return render(request,"encyclopedia/editing.html",{
        "title": title,
        "content": Entry
    })

def saved_entry(request):
    Title=request.GET.get("t")
    Content=request.GET.get("c")
    util.save_entry(Title,Content)
    Entry=util.get_entry(Title)
    return render(request, "encyclopedia/display.html",{
        "searchname": Title,
        "Entry": markdown.markdown(Entry),
        "Title": Title
    })
