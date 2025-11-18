from django.shortcuts import render,redirect
from .models import reg_tbl,Product_tbl,cart_tbl
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,"index.html")
def reg(request):
    if request.method=="POST":
        fnm=request.POST.get("fname")
        mob=request.POST.get("mobile")
        eml=request.POST.get("email")
        pssw=request.POST.get("password")
        cpsw=request.POST.get("cnpassword")
        obj = reg_tbl.objects.create(fname=fnm,mobile=mob,email=eml,pssw=pssw,cpsww=cpsw)
        obj.save()
        if obj:
            return render(request,"log.html")
        else:
            return render(request,"reg.html")
    
    return render(request,"reg.html")

def log(request):
    if request.method=="POST":
        em =request.POST.get("email")
        ps =request.POST.get("password")
        obj = reg_tbl.objects.filter(email=em,pssw=ps)
        if obj:
            request.session['email']=em
            request.session['password']=ps
            for m in obj:
                idno=m.id
            request.session['idl']=idno
            return render(request,"home.html")
        else:
            msg="Invalid email or password"
            request.session['email']=' '
            request.session['password']=' '
            return render(request,"log.html",{'error':msg})  
    return render(request,"log.html")
  

def userdetails(requset):
    obj =reg_tbl.objects.all()
    return render(requset,'user.html',{'data':obj})

def edituser(request,pk):
    obj = reg_tbl.objects.filter(id=pk)
    if request.method=='POST':
        fnm = request.POST.get('fm')
        idl = request.POST.get('idn')
        mob = request.POST.get('mb')
        eml = request.POST.get('em')
        obj = reg_tbl.objects.filter(id=idl)
        obj.update(fname=fnm,mobile=mob,email=eml)
        return redirect('/user')

    return render(request,'oneuser.html',{'data':obj})

def delete(request,pk):
    obj =reg_tbl.objects.filter(id=pk)
    obj.delete()
    return redirect('/user')

def bookdetails(request):
    if request.method=='POST':
        mbn= request.POST.get('mbname')
        mim= request.FILES.get('mbimage')
        prc= request.POST.get('price')
        des= request.POST.get('des')
        obj = Product_tbl.objects.create(mbname=mbn,mbim=mim,prc=prc,dec=des)

        obj.save()
        if obj:
            msg ='Details Uploaded...'
            return render(request,'product.html',{'success':msg})

    return render(request,'product.html')

def bookview(request):
    obj = Product_tbl.objects.all()
    return render(request,'book.html',{'book':obj})



def addtocart(req,pk):
    pobj = Product_tbl.objects.get(id=pk)
    idn = req.session['idl']
    uobj =reg_tbl.objects.get(id=idn)
    cartitem,created=cart_tbl.objects.get_or_create(userobj=uobj,prodobj=pobj)
    if not created:
        cartitem.qty+=1
        cartitem.save()
    messages.success(req,'Product added to cart!....')
    return redirect('/mview')

def viewcart(request):
    idn = request.session['idl']
    obj = reg_tbl.objects.get(id=idn)
    cartuser= cart_tbl.objects.filter(userobj=obj)
    if cartuser:
        total = 0
        for p in cartuser:
            total+=p.prodobj.prc*p.qty
        return render(request,'cart.html',{'data':cartuser,'total':total})
    else:
        return render(request,'cart.html',{'info':"cart is empty...."})   


def cartdelete(request,pk):
    obj =cart_tbl.objects.filter(id=pk)
    obj.delete()
    return redirect('/cart') 





