from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm

import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Create your views here.

config = {

}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def data1(request):
    person = database.child('name').get().val()

    return render(request, 'admin.html', {"name": person})


def say_hello(request):
    form = NameForm()
    return render(request, 'index.html', {'form': form})


def superad(request):
    return render(request, 'admin.html')


def get_name(request):
    x = database.child('count').get().val()
    list1 = []
    flag = 0
    checkuser1 = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            n = form.cleaned_data["name"]
            data = {

                "name": n,
            }

           # database.child('user').child(x).set(data)
           # database.child('count').set(x + 1)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            person = database.child('user').shallow().get().val()
            for i in person:
                list1.append(i)
            list1.sort()
            print(list1)
            for i in list1:
                checkuser1 = database.child("user").child(i).child("name").get().val()
                print(checkuser1)
                if checkuser1 == n:
                    flag = 1
                    break


# if a GET (or any other method) we'll create a blank form
    if flag == 1:
        return render(request, 'admin.html', {"name": checkuser1})
    else:
        return HttpResponseRedirect("/home")
        # form = NameForm()


