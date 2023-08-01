from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TheList, Item
from .forms import CreateNewList


def index(request, pk):
    the_list = TheList.objects.get(id=pk)
    return render(request, "main/base.html", {"the_list": the_list})


def view_list(request, pk):
    the_list = TheList.objects.get(id=pk)
    if the_list in request.user.thelist.all():
        if request.method == "POST":
            print(request.POST)
            if request.POST.get("save"):
                for item in the_list.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.status = True
                    else:
                        item.status = False
                    item.save()
            elif request.POST.get("newItem"):
                txt = request.POST.get("newItemText")
                if len(txt) > 2:
                    the_list.item_set.create(text=txt, status=False)
                else:
                    print("invalid input")
            elif request.POST.get("deleteList"):
                return HttpResponseRedirect("/confirmation_%i" % the_list.id,
                                            {"pk": pk, "the_list": the_list})
        return render(request, "main/view_list.html", {"the_list": the_list})
    return render(request, "main/home.html", {})


def confirmation(request, pk):
    the_list = TheList.objects.get(id=pk)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("yes"):
            the_list.delete()
            return HttpResponseRedirect("/")
        if request.POST.get("no"):
            return HttpResponseRedirect("/%i" % the_list.id)
    return render(request, "main/confirmation.html", {"the_list": the_list})


def home(request):
    return render(request, "main/home.html", {})


def new_list(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data["name"]
            the_list = TheList(name=form_name)
            the_list.save()
            request.user.thelist.add(the_list)
            return HttpResponseRedirect("/%i" % the_list.id)
        return HttpResponseRedirect("main/new_list.html")
    else:
        form = CreateNewList()
    return render(request, "main/new_list.html", {"form": form})


def latestlist(request):
    # last = request.user.thelist.last()
    # print(last)
    # TheList.objects.last()
    beep = request.user.thelist.last()
    ms = 'are you feeling it, mr krabs?'
    mynum = 20
    return render(request, "main/latest_list.html",
                  {"beep": beep, "ms": ms, "mynum": mynum})
