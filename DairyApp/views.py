from django.shortcuts import render
from .models import Farmer,MilkData
from django.template import loader
from django .http import HttpResponse

def home(request):
    return render(request,'Home.html')

def cfarmer(request):
    return render(request,'create_farmer.html')

def fsave(request):
    template = loader.get_template('create_farmer.html')
    Id= request.POST['fid']
    Name=request.POST['fname']
    f = Farmer(Id, Name)
    if int(Id) >= 200:
        con={'fail_msg':"the farmer id can't morethan 200"}
        '''d={}
        for each in range(int(Id)):
            d[each]=each
        con['d']=d'''
        return HttpResponse(template.render(con,request))
    else:
        f.save()
        context = {'success_msg':"svaed record successfully"}
        #return HttpResponse("<h1>record inserted successfully</h1>")
        return HttpResponse(template.render(context, request))
        #return render(request,'create_farmer.html',{'msg':'<h1>record inserted successfully</h1>'})

def showFarmers(request):
    records = Farmer.objects.all()
    return render(request,'show.html',{'recs':records})

def milkent(request):
    return render(request,'milk.html')

def msave(request):
    template = loader.get_template('milk.html')
    d = request.POST['date']
    fid = request.POST['fid']
    mq = request.POST['milkqty']
    ft = request.POST['fat']
    rt = request.POST['rate']
    tm = request.POST['totalamt']
    ms = MilkData(d,fid,mq,ft,rt,tm)
    ms.save()
    con = {'success_msg':"record inserted successfully"}
    return HttpResponse(template.render(con,request))

def sFarmers(request):
    return render(request,'show.html')

def showMilk(request):
    records = MilkData.objects.all()
    #import pdb
    #pdb.set_trace()
    for each in records:
        each.fname = Farmer.objects.get(fid=str(each.fid_id)).fname

    #records = Farmer.objects.get('fname')
    return render(request,'show2.html',{'recs':records})

def deleteFarmer(request):
    return render(request,'delete.html')

def removeFarmer(request):
    template = loader.get_template('show.html')
    t1=request.POST['t1']
    Farmer.objects.get(fid=t1).delete()
    con = {'recs': Farmer.objects.all()}
    return HttpResponse(template.render(con, request))

def mpage(request):
    return render(request,'mypage.html')

def mcal(request):
    template=loader.get_template('mypage.html')
    con = {'msg': "the numbers are:"}
    I=request.POST['num']
    d = []
    #if I<=100:
    for each in range(int(I)):

        #d[each] = each
        d.append(each)
    n = dict([(x,y) for x,y in zip(d[::2],d[1::2])])
    con['d'] = n
    return HttpResponse(template.render(con,request))

def login(request):
        return render(request,'login.html')

def loginval(request):
    #template=loader.get_template('login.html')
    name=request.POST['uname']
    word = request.POST['pid']
    if name=="aseeth" and word == "aseeth":
        return render(request,'Home.html')
    else:
        #con = {'msg':'please enter valid mail id & password'}
        return HttpResponse("<h1>please enter valid mail id & password</h1>")

def dobb(request):
    l=[]
    template = loader.get_template('mypage.html')
    context={'db':"Your date of birth is:"}
    d=request.POST['day']
    m=request.POST['month']
    y=request.POST['year']
    z=int(31)-int(d)
    yy =int(12)-int(m)
    x =int(2018)-int(y)

    #context={'db':"your dob is" }
    return HttpResponse(template.render(context,request))

def emilkPage(request):
    return render(request,"Emilk.html")

def eMilk(request):
    #MilkData.objects.filter(fid=request.POST['t1']).update(milkqty=request.POST['t2'])
    #return HttpResponse("<h4>Updated Successfully</h4>")

    template = loader.get_template('show2.html')
    t1 = request.POST['t1']
    t2 = request.POST['t2']
    MilkData.objects.filter(fid=t1).update(milkqty=t2)
    con = {'recs': MilkData.objects.all()}
    return HttpResponse(template.render(con, request))

########################################################
########################################################
################Rerurn Json Data########################
########################################################
########################################################

from django.http import JsonResponse

def some_view(request):
    data = list(Farmer.objects.values())
    #return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
    return JsonResponse({'data': data})
