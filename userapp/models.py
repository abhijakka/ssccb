from django.db import models  
from adminapp.models import *
from django.forms import ClearableFileInput

class UserRegisration(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    profile_photo=models.ImageField(upload_to='images/',null=True)   
    password=models.CharField(max_length=50)
    status=models.CharField(default='Accepted',max_length=500,null=True)
    sum_self_download=models.BigIntegerField(help_text='sum_self_download',default=0)
    no_uploads=models.BigIntegerField(help_text='no_uploads',default=0)
    upload_file_size=models.BigIntegerField(help_text='no_uploads',default=0)
    public_downloads=models.BigIntegerField(help_text='public_downloads',default=0)

   
    class Meta:
         db_table = 'user_details'  
         
class UploadFiles(models.Model):
    file_id=models.AutoField(primary_key=True)
    file_name=models.CharField(help_text='file_name',max_length=50,null=True)
    file_password=models.CharField(help_text='file_password',max_length=50,null=True)
    upload_files=models.FileField(help_text='upload_files',max_length=100,null=True)
    file_size=models.CharField(help_text='file_size',max_length=50,null=True)
    public_key=models.CharField(help_text='public_key',max_length=5000,null=True)
    private_key=models.CharField(help_text='private_key',max_length=5000,null=True)
    encrypted_key=models.CharField(help_text='encrypted_key',max_length=5000,null=True)
    discribtion=models.TextField(help_text='discribtion',null=True)
    self_download=models.BigIntegerField(help_text='self_download',default=0,null=True)
    users_download=models.BigIntegerField(help_text='users_download',default=0,null=True)
    
    user_id=models.ForeignKey(UserRegisration,models.CASCADE,null=True)
    url_id=models.ForeignKey(short_urlss,models.CASCADE,null=True)
    
    class Meta:
        db_table='UploadFiles'
          
        
from django import forms      
class ResumeUpload(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ["upload_files"]
        widgets = {
            "upload_files": ClearableFileInput(attrs={'multiple': True}),
        }         


class user_key_uploaded(models.Model):
    fileno=models.AutoField(primary_key=True)
    UploadFiles=models.ForeignKey(UploadFiles,on_delete=models.CASCADE,null=True)
    user_id=models.ForeignKey(UserRegisration,models.CASCADE,null=True)
    privatekeyfile=models.FileField(upload_to='uploadedkey',help_text='privatekeyfile',null=True)
    decrypted_key=models.CharField(help_text='decrypted_key',max_length=5000,null=True)
    class Meta:
        db_table='privatekey_Uploaded_details'                     
        
        
class ipaddress(models.Model):
    ipaddress_id=models.AutoField(primary_key=True) 
    ipaddress=models.CharField(max_length=200,help_text='ipaddress',null=True)
    
    ipaddress_date=models.DateField(auto_now_add=True,null=True)
    ipaddress_time=models.TimeField(auto_now_add=True,null=True)
    existed_ipaddress_datetime=models.DateTimeField(auto_now_add=True,null=True)
    existed_ip_count=models.BigIntegerField(help_text='existed_ip_count', default=0)
    
    class Meta:
            db_table='ipaddress'
# class existipaddress(models.Model):
#       p_id=models.AutoField(primary_key=True)  
#       exist_ipaddress_date=models.CharField(max_length=200,help_text='exist_ipaddress_date',null=True)
#       exist_ipaddress_time=models.TimeField(auto_now_add=True,null=True)
#       ipaddress_id=models.ForeignKey(ipaddress,on_delete=models.CASCADE,null=True)
#       exist_ipaddress=models.CharField(max_length=200,help_text='ipaddress',null=True)
#       class Meta:
#             db_table='exist_ipaddress'        
  
