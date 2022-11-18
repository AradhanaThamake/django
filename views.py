from turtle import title
from django.http import HttpResponse
from django.shortcuts import  render,redirect
from django.http import HttpResponse
from todoapp.models import Task

# Create your views here.
def home(request):

    #return HttpResponse('Hello Home Page')
    #return redirect('/contact')
    #return render(request,'home.html')
    d={'id':12,'name':'kajal','rno':30}
    return render(request,'home.html',d)

def product(request):

    data="Hello From Product" 
    return HttpResponse(data)

def contact(request):

    data="<h1>Hello From Contact Page</h1>"     
    return HttpResponse(data)


def edit(request,rid):

    #data="ID to be edited is:"+rid
    #return HttpResponse(data)
    if request.method=="POST":
        ut=request.POST['t']
        udet=request.POST['det']
        udt=request.POST['dt']
        #print(ut)
        #print(udet)
        #print(udt)
        
        x=Task.objects.filter(id=rid)
        x.update(title=ut,detail=udet,date=udt)
        #update todoapp_task SET title=ut,detail=uder,date=udt 
        return redirect('/')
    else:
        content={}  
        content['data']=Task.objects.filter(id=rid) 
        return render(request,'editform.html',content) 

def delete(request,rid):
    '''
        data="ID to be deleted is:"+rid

    return HttpResponse(data)    

    '''
    '''
    #hard delete code
    
    x=Task.objects.get(id=rid)
    x.delete()
    return redirect('/')
    '''
    
    x=Task.objects.filter(id=rid)
    x.update(is_deleted='Y')
    return redirect('/')
    
    
def evenodd(request,n):

    r=int(n)%2
    d={'res':r}
    return render(request,'home.html',d)


def loop(request):
    d={
        'l':[10,20,30,40,50,60]
    }
    return render(request,'home.html',d)

def index(request):
    
    content={}
    #content['data']=Task.objects.all()
    content['data']=Task.objects.filter(is_deleted='N')
    #print(content['date'])
    
    return render(request,'index.html',content)

def about(request):

    return render(request,'about.html')

def create_task(request):
    
    if request.method=='POST':
        t=request.POST['t']
        det=request.POST['det']
        dt=request.POST['dt']
        #print(t)
        #print(det)
        #print(dt)
        t1=Task.objects.create(title=t,detail=det,date=dt,is_deleted='N')
        #print(t1)
        t1.save()
        return redirect('/')
    else:
        return render(request, 'create_task.html')
    
