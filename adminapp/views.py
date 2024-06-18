from django.shortcuts import render,redirect,get_object_or_404
from adminapp.models import *
from userapp.models import *
from ssccb.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.db.models import Sum
from django.contrib import messages

from django.core.paginator import Paginator

# Create your views here.
def admin_dashboard(request):
    try:
      request.session['email']
    except:
        return redirect('home')
    pending=UserRegisration.objects.filter(status='pending').count()
    accepted=UserRegisration.objects.filter(status='Accepted').count()
    rejected=UserRegisration.objects.filter(status='Rejected').count()
    total=UserRegisration.objects.all().count()
    data=UserRegisration.objects.filter(status='pending')
    paginator = Paginator(data, 10)
    page_number =request.GET.get('page')
    print(paginator)

    page_obj = paginator.get_page(page_number)

    print(page_obj)
    
    return render(request,'admin/admin-index.html',{'pending':pending,'accepted':accepted,'rejected':rejected,'total':total,'data':data,"page_obj":page_obj})

def admin_cmastatus(request):
    try:
      request.session['email']
    except:
        return redirect('home')
    data=UserRegisration.objects.filter(status='Accepted').all()
    paginator = Paginator(data, 10)
    page_number =request.GET.get('page')
    print(paginator)

    page_obj = paginator.get_page(page_number)

    print(page_obj)
    
    
    return render(request,'admin/admin-user-datastatus.html',{'data':data,"page_obj":page_obj})

def admin_userrequest(request):
    try:
      request.session['email']
    except:
        return redirect('home')
    data=UserRegisration.objects.order_by('-user_id')
    paginator = Paginator(data, 10)
    page_number =request.GET.get('page')
    print(paginator)

    page_obj = paginator.get_page(page_number)

    print(page_obj)
    
    return render(request,'admin/admin-user-request.html',{'data':data,"page_obj":page_obj})

def user_accept(request,id):
        accept = get_object_or_404(UserRegisration,user_id=id)
        accept.status = 'Accepted'
        accept.save(update_fields=['status']) 
        accept.save()   
        html_content = "<br/><p>SHARE Want to inform you that Your Regisration  Request is <b>accepted</b> by team of SHARE as it is issued by a share\
           <br>Thanks for your Resgistration</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [accept.email ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Your SHARE Registration Status ", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
          if msg.send():
               print("Sent")
               return redirect('admin_userrequest')
        except: 
             return redirect('admin_userrequest')      
        return redirect('admin_userrequest')
    
def user_reject(request,id):
        reject = get_object_or_404(UserRegisration,user_id=id)
        reject.status = 'Rejected'
        reject.save(update_fields=['status']) 
        reject.save()   
        html_content = "<br/><p>SHARE Want to inform you that Your Regisration  Request is <b>Rejected</b> by team of SHARE as it is issued by a share\
           <br>Thanks for your Resgistration</p>"
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [reject.email ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("Your SHARE Registration Status ", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
          if msg.send():
               print("Sent")
               return redirect('admin_userrequest')
        except: 
             return redirect('admin_userrequest')      
        return redirect('admin_userrequest')


def new_ipaddress(request):
    try:
      request.session['email']
    except:
        return redirect('home')
    data=ipaddress.objects.all().order_by("-ipaddress_id")
    paginator = Paginator(data, 10)
    page_number =request.GET.get('page')
    print(paginator)

    page_obj = paginator.get_page(page_number)

    print(page_obj)
    
    return render(request,'admin/admin-user-new-ip.html',{"data":data,"page_obj":page_obj})



def User_admin(request):
    if request.method=="POST" and "btn55" in request.POST: 
        email=request.POST.get('email')       
        html_content = "<br/><p>SUBCRIBER REQUEST</p>"
        from_mail = email
        to_mail = [DEFAULT_FROM_EMAIL ]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives("SHARE REQUEST", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        try:
            if msg.send():
                print(msg)
                message=messages.success(request,'email has been sent,')
        except:
            message=messages.error(request,'email has been Failed,Try Again ')
            pass
    elif request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('psw')
        if email == "admin@gmail.com" and password == "admin":
            request.session["email"]=email
            return redirect('admin_index')
        else:
            message=messages.error(request,'email or password incorrect,Try Again ')

         
    
    return render(request,'user/user-login.html')

