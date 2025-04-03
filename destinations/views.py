from django.shortcuts import render
from activities.views import activities_data
from .datas import destinations_data
# Create your views here.
def destination_list(request):
    typeset={x['type'] for x in destinations_data}
    context={
        'dlist':destinations_data,
        'typelist':typeset,
    }
    return render(request,'destination_list.html',context)
def destination_details(request,id):
    data=None
    for x in destinations_data:
        if x['id']==id:
            data=x
    context={
        'data':data,
        'activities':activities_data,
    }
    return render(request,'destination_details.html',context)
def index(request):return render(request,'index.html')
