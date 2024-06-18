from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from adminapp.models import *
import rsa
import json
import requests
import os.path
from django.contrib import messages

from userapp.form import UrlForm
from userapp.shortner import shortner
from ssccb.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
import smtplib
from django.db.models import Q,F
from django.http import JsonResponse,HttpResponse
from ssccb import settings
from time import sleep
from datetime import datetime
from django.core.paginator import Paginator


# Create your views here.


def Home(request):
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            
        return ip
    get_client_ip(request)
    a=get_client_ip(request)
    b=request.session['ipaddress']=a
    print(a)
   
    
    check=ipaddress.objects.filter(ipaddress=a).exists()
    if check:
        data5=ipaddress.objects.get(ipaddress=b)
        data5.existed_ipaddress_datetime=datetime.now()
        data5.save(update_fields=['existed_ipaddress_datetime'])
        
        data6=ipaddress.objects.filter(ipaddress=b).update(existed_ip_count=F('existed_ip_count')+1)
        
        
        
         
    else:
        ipaddress.objects.create(ipaddress=a) 
        
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
               
    
    return render(request,'user/index.html',{"ip":a})


def About(request):
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
    return render(request,'user/about.html')


def Contact(request):
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
    return render(request,'user/contact.html')




def User_index(request):
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
        
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
    return render(request,'user/user-index.html')




def User_about(request):
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
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
    return render(request,'user/user-about.html')


def Upload_files(request):
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
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
    data3=UserRegisration.objects.get(user_id=user)
    
    if request.method =='POST' :
        # form = ResumeUpload(request.POST, request.FILES)
        # files = request.FILES.getlist("file_image") 
        file_name=request.POST.get('file_name')
        file_password=request.POST.get('password')
        describtion=request.POST.get('file_describition')
        file=request.FILES.getlist('file_image')
        print(file,'jdskkkkkkkkkkkkkdshjhjdshhfds')
        
            
       
        data5=UploadFiles.objects.filter(file_name=file_name).exists()
        if data5:
            message=messages.error(request,'file name already exists please try New Name')  
        else:
        
        
            public_key, private_key = rsa.newkeys(1024)
            
            with open(os.path.join('media\orginalpem',file_name+"public.pem"), "wb") as public:
              public.write(public_key.save_pkcs1("PEM"))
            
            with open(os.path.join('media\orginalpem',file_name+"private.pem"), "wb") as fb:
             fb.write(private_key.save_pkcs1("PEM"))
             ac=str(fb)
             ab=ac[26:-2]
             print(ab)
        
            with open(os.path.join('media\orginalpem',file_name+"public.pem"), "rb") as f:
             public_key = rsa.PublicKey.load_pkcs1(f.read())
            # with open(os.path.join('media\orginalpem',file_name+"private.pem"), "rb") as f:
            #  private_key = rsa.PrivateKey.load_pkcs1(f.read())
            message = file_password
            encrypted_message = rsa.encrypt(message.encode(), public_key)
            
            with open(os.path.join('media\orginalpem',file_name+"encrypted.message"), "wb") as f:
             f.write(encrypted_message)
            print(private_key,'abhi')
            print(public_key,'abhu848')
            for filess in file:
               
                
                a=filess.size
                data=UploadFiles.objects.create(file_name=file_name,file_password=file_password,
                                            upload_files=filess,discribtion="NULL",public_key=file_name+'public.pem'
                                        ,private_key=file_name+'private.pem',encrypted_key=encrypted_message,file_size=a,user_id=data3)
                data100=UserRegisration.objects.get(user_id=user)
                data100.no_uploads=data100.no_uploads+1
                data100.upload_file_size=data100.upload_file_size+int(a)
                data100.save(update_fields=['no_uploads','upload_file_size'])
                
            try:
                html_content =  "<br/> <p> Your Private Key .</p>"
                from_mail = DEFAULT_FROM_EMAIL
                to_mail = [data3.email]
                msg = EmailMultiAlternatives("SHARE Application Status",html_content,from_mail,to_mail)
                msg.attach_alternative(html_content,"text/html")
                file= ab
                msg.attach_file(file)
                
        
                try:
                    if msg.send():
                        print(msg)
                        message=messages.success(request,'Privatekey has been sent,')
                        

                except:
                    message=messages.error(request,'Privatekey has been Failed,Try Again ')
                    pass
                  
            except:
                #  path=str(dz.upload_files)
                #         with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as fh:
                            response = HttpResponse(content_type=file)
                            response['Content-Disposition'] = 'attachment; filename='+ str(file)   
                            return response   
            
        
    
    return render(request,'user/uploadfiles.html')


def Myfiles(request):
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
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
    data=UploadFiles.objects.filter(user_id=user).order_by('-file_id')
    data2=UploadFiles.objects.filter(user_id=user).order_by('-file_id')
    
    # paginator = Paginator(data,8)

    # page_number =request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # pages = page_obj.paginator.num_pages
    paginator = Paginator(data, 10)
    page_number =request.GET.get('page')
    print(paginator)

    page_obj = paginator.get_page(page_number)

    print(page_obj)
    
    
    
    return render(request,'user/myfile.html',{'data':data,"page_obj":page_obj,"data2":data2})

def Make (request,id):
    form=UrlForm(request.POST)
    data3=UploadFiles.objects.get(file_id=id)
    az=data3.file_id
    name='http://127.0.0.1:8000/publicfile/'
    name2='http://127.0.0.1:8000/'
      
    NewUrl = id
    a = shortner().issue_token()
    NewUrl = a
        
    print(NewUrl)
    bc=str(id) 
    
    data=short_urlss.objects.create(short_url=NewUrl,long_url=name+bc,file_id=az,complete_short_url=name2+a)
    data5=short_urlss.objects.get(file_id=id)
    data2=UploadFiles.objects.get(file_id=id)
    data2.url_id=data5
    data2.save(update_fields=['url_id'])
    
    return redirect('myfiles')  



def filedownload(request,id):
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
        
        
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
   
    data=UploadFiles.objects.get(file_id=id)
    file_name=data.file_name
    
    # da=user_key_uploaded.objects.get(UploadFiles=id)
    # data5=get_object_or_404(user_key_uploaded,UploadFiles=id)
    data4=user_key_uploaded.objects.filter(user_id=user).filter(UploadFiles=id)
    try:
        data20=user_key_uploaded.objects.filter(UploadFiles=id)
    except:    
       data20=user_key_uploaded.objects.get(UploadFiles=id) 
    
    if request.method=='POST'   :
        filename=request.POST.get('name')
          
        if request.method=='POST' and request.FILES.get('file'):
            file=request.FILES['file']
            
            data6=user_key_uploaded.objects.filter(UploadFiles=id).exists()
            if data6 :
                
                data53=get_object_or_404(user_key_uploaded,UploadFiles=id)
                data53.privatekeyfile=file
                data53.save(update_fields=['privatekeyfile'])
            else:
                data2=UploadFiles.objects.get(file_id=id)
                data3=UserRegisration.objects.get(user_id=user)
                data10=user_key_uploaded.objects.create(privatekeyfile=file,UploadFiles=data2,user_id=data3)
            for i in data4:
                fileupload=i.privatekeyfile
            path='media/'+ str(fileupload)
            print(path)
            try:
                with open(path, "rb") as f:
                    private_key = rsa.PrivateKey.load_pkcs1(f.read())
                    encrypted_message = open(os.path.join('media\orginalpem',file_name+"encrypted.message"), "rb").read()
                    clear_message = rsa.decrypt(encrypted_message, private_key)
                    d=(clear_message.decode())
                    print(clear_message.decode())
                
                    data13=get_object_or_404(user_key_uploaded,UploadFiles=id)
                    data13.decrypted_key=d
                    data13.save(update_fields=['decrypted_key'])
                     
                    if data13:
                        path=str(data.upload_files)
                        with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as fh:
                            response = HttpResponse(fh.read(), content_type=data.upload_files)
                            response['Content-Disposition'] = 'attachment; filename='+ str(data.upload_files)   
                            return response
                         
                                    
            except:
                    data63=get_object_or_404(user_key_uploaded,UploadFiles=id)
                    data63.privatekeyfile='fail'                                                                                                                                                                            
                    data63.save(update_fields=['decrypted_key','privatekeyfile'])
                    message=messages.error(request,'worng Key please try again') 
                    pass
            finally:
                data55=get_object_or_404(user_key_uploaded,UploadFiles=id)
                data55.decrypted_key='fail'
                data55.privatekeyfile='fail'
                data55.save(update_fields=['decrypted_key','privatekeyfile'])
                data96=get_object_or_404(UploadFiles,file_id=id)
                data96.self_download=data96.self_download+1
                
                
                data96.save(update_fields=['self_download'])
                data100=UserRegisration.objects.get(user_id=user)
                data100.sum_self_download=data100.sum_self_download+1
                data100.save(update_fields=['sum_self_download'])
                
               
        if not request.FILES.get('file'):
                message=messages.warning(request,'Please Upload file')
                data56=get_object_or_404(user_key_uploaded,UploadFiles=id)
                data56.decrypted_key='fail'
                data56.privatekeyfile='fail'
                data56.save(update_fields=['decrypted_key','privatekeyfile'])
                        
    
      
    
    return render(request,'user/download.html',{'data':data,'data20':data20})

def public_download(request,id):
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
    data=UploadFiles.objects.filter(file_id=id)
    for dz in data:
        file_name=dz.file_name
        a1=dz.upload_files
        print(file_name,a1)
    
    data4=user_key_uploaded.objects.filter(UploadFiles=id)
    try:
        data20=user_key_uploaded.objects.filter(UploadFiles=id)
    except:    
       data20=user_key_uploaded.objects.filter(UploadFiles=id)
    if request.method=='POST'   :
        filename=request.POST.get('name')
          
        if request.method=='POST' and request.FILES.get('file'):
            file=request.FILES['file']
            
            data6=user_key_uploaded.objects.filter(UploadFiles=id).exists()
            if data6 :
                
                data53=get_object_or_404(user_key_uploaded,UploadFiles=id)
                data53.privatekeyfile=file
                data53.save(update_fields=['privatekeyfile'])
            else:
                data2=UploadFiles.objects.get(file_id=id)
                
                data10=user_key_uploaded.objects.create(privatekeyfile=file,UploadFiles=data2)
            for i in data4:
                fileupload=i.privatekeyfile
            path='media/'+ str(fileupload)
            print(path) 
            try:
                with open(path, "rb") as f:
                    private_key = rsa.PrivateKey.load_pkcs1(f.read())
                    encrypted_message = open(os.path.join('media\orginalpem',file_name+"encrypted.message"), "rb").read()
                    clear_message = rsa.decrypt(encrypted_message, private_key)
                    d=(clear_message.decode())
                    print(clear_message.decode())
                
                    data13=get_object_or_404(user_key_uploaded,UploadFiles=id)
                    data13.decrypted_key=d
                    data13.save(update_fields=['decrypted_key'])
                    
                    if data13:
                        path=str(dz.upload_files)
                        with open(os.path.join(settings.MEDIA_ROOT, path), 'rb') as fh:
                            response = HttpResponse(fh.read(), content_type=dz.upload_files)
                            response['Content-Disposition'] = 'attachment; filename='+ str(dz.upload_files)   
                            return response
                            
                
                                    
            except:
                    data63=get_object_or_404(user_key_uploaded,UploadFiles=id)
                    data63.privatekeyfile='fail'                                                                                                                                                                            
                    data63.save(update_fields=['decrypted_key','privatekeyfile'])
                    message=messages.error(request,'worng Key please try again') 
                    pass
                
            else:
                
                return redirect('home')
            
            finally:
                
                  
                data55=get_object_or_404(user_key_uploaded,UploadFiles=id)
                data55.decrypted_key='fail'
                data55.privatekeyfile='fail'
                data55.save(update_fields=['decrypted_key','privatekeyfile'])
                data96=get_object_or_404(UploadFiles,file_id=id)
                data96.users_download=data96.users_download+1
                us=data96.user_id.email
                data96.save(update_fields=['users_download'])
                print('hiiiiiiiii this abhi')
                count=UserRegisration.objects.filter(email=us).update(public_downloads=F('public_downloads')+1)
                
                
            
                
               
        if not request.FILES.get('file'):
                data56=get_object_or_404(user_key_uploaded,UploadFiles=id)
                data56.decrypted_key='fail'
                data56.privatekeyfile='fail'
                data56.save(update_fields=['decrypted_key','privatekeyfile'])
                        
    if request.method=='POST' and 'btn2' in request.POST:
        print('abhi45455')
        
        fail=request.POST.get('fail')
        data55=get_object_or_404(user_key_uploaded,UploadFiles=id)
        data55.decrypted_key='fail'
        data55.privatekeyfile='fail'
        data55.save(update_fields=['decrypted_key','privatekeyfile'])
        data96=get_object_or_404(UploadFiles,file_id=id)
        data96.users_download=data96.users_download+1
        data96.save(update_fields=['users_download'])
        # return redirect('home')
    return render(request,'user/public_download.html',{'data':data,'data20':data20})
def Myprofile(request):
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
    return render(request,'user/myprofile.html')




def Admin_login2(request):
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
    try:
         user=request.session['user_id']
    except:
        return redirect('home')
    data=UserRegisration.objects.get(user_id=user)
    if request.method=='POST':
        password=request.POST.get('password')
        data.password=password
        data.save(update_fields=['password'])
        if data:
            messages.success(request,' succesfully Updated') 
    
    return render(request,'user/admin2.html',{'data':data})




# def User_login(request):
    
    
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('psw')
#         clientkey=request.POST.get('g-recaptcha-response')
        
#         print('key',clientkey)
#         secretKey = '6LfPTIgkAAAAAPIfmy6fEFpOOqCaJJ3qqHLAeeJD'
#         data={
#         'secret': secretKey,
#         'response': clientkey
#         }
#         r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
       
#         response=json.loads(r.text)
#         verify=response['success'] 
#         c=(str(verify))
#         if c == 'True': 
#             try:
#                 if email=='admin@gmail.com' and  password =='admin' :
#                     print(email,'pass',password)
#                     message=messages.success(request,'login success')
#                     return redirect('admin_index')  
#                 check = UserRegisration.objects.get( email=email, password=password) 
#                 print(check,'sjdfkckjjsakjdnskjadnksadkskanskjaskjakf')
#                 request.session['user_id']=check.user_id 
                
#                 status = check.status
#                 if status =='Accepted':
#                     message=messages.success(request,'login success')
#                     return redirect('User_index') 
#                 elif status =='Rejected' : 
#                     message=messages.error(request,'Your request is Rejected so you cannot login')  
#                 elif status == 'pending':
#                     message=messages.info(request,'Your request is Pending so cannot login')
                    
#             except:
#                 messages.warning(request,'invalid login')
#                 print('fail') 
                
           
                
                 
#         else:
#              messages.warning(request,'please enter human captcha!')       
    
#     return render(request,'user/user-login.html')

def User_register(request):
    if request.method=="POST" and "btn55" in request.POST: 
        email=request.POST.get('email55')       
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
            name=request.POST.get('uname') 
            email=request.POST.get('Email') 
            
            # profile_photo=request.FILES['photo'] 
            password=request.POST.get('psw')
            print(name,password,email,'ajshhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            path='assets/static/user/pic.jpg'                             # file path of image
            from django.core.files import File as DjangoFile              #library
            file_obj1 = DjangoFile(open(path, mode='rb'), name='pic.jpg') # saving image in media where name='pic.jpg' is saving iamge name
            data=UserRegisration.objects.create(name=name,email=email,
                                                profile_photo=file_obj1,
                                                password=password)
           
            if data:
                 html_content = "<br/><p>SSCCB Want to inform you that Your Regisration  Request is <b>accepted</b> by team of SSCCB as it is issued by a share\
                 <br>Thanks for your Resgistration</p>"
                 from_mail = DEFAULT_FROM_EMAIL
                 to_mail = [email ]
                  # if send_mail(subject,message,from_mail,to_mail):
                 msg = EmailMultiAlternatives("Your SSCCB Registration Status ", html_content, from_mail, to_mail)
                 msg.attach_alternative(html_content, "text/html")
                 try:
                    if msg.send():
                        print("Sent")
                    
                 except: 
                    pass
                 messages.success(request,' succesfully Registered') 
            else:        
                 messages.error(request,' please Try Again ') 
    
    return render(request,'user/user-register.html')

def User_login(request):
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
        # if email == "admin@gmail.com" and password == "admin":
        #     request.session["email"]=email
        #     return redirect('admin_index')
        try:
                check = UserRegisration.objects.get(email=email,password=password)  
                request.session['user_id']=check.user_id 
                
                status = check.status
                
                if status =='Accepted':
                    message=messages.success(request,'login success')
                    return redirect('User_index') 
                elif status =='Rejected' : 
                    message=messages.error(request,'Your request is Rejected so you cannot login')  
                elif status == 'pending':
                    message=messages.info(request,'Your request is Pending so cannot login')
                
        except:
                messages.warning(request,'invalid login') 
    
    return render(request,'user/user-login.html')


# def User_register(request):
#     if request.method == 'POST' and 'photo' in request.FILES:
#            name=request.POST.get('uname') 
#            email=request.POST.get('Email') 
            
#            profile_photo=request.FILES['photo'] 
#            password=request.POST.get('psw') 
#            data=UserRegisration.objects.create(name=name,email=email,
#                                                profile_photo=profile_photo,
#                                                password=password)
#            if data:
#                messages.success(request,' succesfully Registered') 
    
    
#     return render(request,'user/user-register.html')


# def User_register(request) :
    
#     if request.method == 'POST' : 
#         name=request.POST.get('uname') 
#         email=request.POST.get('Email')
#         print(email) 
#         # dob=request.POST.get('date')  
#         password=request.POST.get('psw')
        
        
#         # Recaptcha stuff
#         clientkey=request.POST.get('g-recaptcha-response') # g-recaptcha-response is default for human captcha please dont modify
        
#         print('keyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',clientkey)
#         secretKey = '6LfPTIgkAAAAAPIfmy6fEFpOOqCaJJ3qqHLAeeJD'
#         data={
#         'secret': secretKey,
#         'response': clientkey
#         }
#         r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
       
#         response=json.loads(r.text)
#         verify=response['success'] 
#         c=(str(verify))
#         if c == 'True' : 
#             data2=UserRegisration.objects.filter(email=email).exists() or email=='admin@gmail.com' and  password =='admin'
#             if data2:
#                 messages.error(request,'You are already registered with this email')
#             else:    
#             #image
#                 path='assets/static/user/pic.jpg'                             # file path of image
#                 from django.core.files import File as DjangoFile              #library
#                 file_obj1 = DjangoFile(open(path, mode='rb'), name='pic.jpg') # saving image in media where name='pic.jpg' is saving iamge name
                
#                 # data=UserRegisration.objects.create(name=name,email=email,profile_photo=file_obj1,password=password,date_of_birth=dob)
                
                
#                 data=UserRegisration.objects.create(name=name,email=email,
#                                                profile_photo=file_obj1,
#                                                password=password)
#                 if data:
#                     messages.success(request,' succesfully Registered')
#         else:
#             messages.warning(request,'please enter human captcha!')       
                
                
#     return render(request,'user/user-register.html')

def forget_password(request):
    if request.method == 'POST' :
        email = request.POST.get('email')
        print(email)
        check=UserRegisration.objects.filter(email=email).exists()
        print(check)
        if check:
            import string    
            import random # define the random module  
            S = 10  # number of characters in the string.  
            # call random.choices() string module to find the string in Uppercase + numeric data.  
            ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
            random1=ran # print the random data
            
            html_content = "<br/> <p> Your Email:</p>"+email+"<br/> <p> Your password:</p>"+random1+"<br/> <p> After Login You Can Change Your Password</p>"+"<br><p>Thanks You:</p>"+"<br><p>SHARE</p>"
            
            from_mail = DEFAULT_FROM_EMAIL
            to_mail = [email]
            msg = EmailMultiAlternatives("SHARE Application Status",html_content,from_mail,to_mail)
            msg.attach_alternative(html_content,"text/html")
            # file= ab
            # msg.attach_file(file)
            
    
            try:
                if msg.send():
                    print(msg)
                    message=messages.success(request,'Password has been sent,')
                    

            except:
                message=messages.error(request,'Password has been Failed,Try Again ')
                pass
            
        else:
             message=messages.error(request,'Email is not Registered! ')   
            
    return render(request,'user/forget-password.html')


def session_del(request):
    try:
       del request.session['user_id']
    except:
        del request.session['email']
    
    return redirect('home')





def shortlink (request,token): 
    long_url = short_urlss.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)





 




