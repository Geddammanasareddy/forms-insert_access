from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic insertion is successfully done')
    return render(request,'insert_topic.html')




def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST.get('name')
        url=request.POST.get('url')
        email=request.POST['email']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()

        return HttpResponse('webpage insertion is successfully done')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    LOT=Webpage.objects.all()
    d={'name':LOT}


    if request.method=='POST':
        name=request.POST.get('name')
        author=request.POST.get('author')
        date=request.POST.get('date')


        WO=Webpage.objects.get(name=name)
        AO=AccessRecords.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('Accessrecords is successfully done')
    return render(request,'insert_access.html',d)
















