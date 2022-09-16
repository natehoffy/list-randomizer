from django.shortcuts import render
from .list_randomizer import list_randomizer


def button(request):
    pse = ['Ashley', 'David', 'Dave', 'Haz', 'Kari', 'Steve', 'Tim']
    return render(request,'home.html', {'data': "PSE List - SEP 2022: " + str(pse)})


def output(request):
    this_list = ['Ashley', 'David', 'Dave', 'Haz', 'Kari', 'Steve', 'Tim']
    data = list_randomizer(this_list)

    return render(request, 'home.html', {'data': "PSEs in Alphabetical Order: " + str(this_list) +
                                                 " Randomly ordered list of PSEs: " + str(data)})
