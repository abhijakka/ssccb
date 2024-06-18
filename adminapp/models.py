from django.db import models

# Create your models here.
class short_urlss(models.Model):
    url_id = models.AutoField(primary_key=True)
    short_url=models.CharField(help_text='decrypted_key',max_length=5000,null=True)
    complete_short_url=models.CharField(help_text='complete_short_url',max_length=5000,null=True)
    long_url = models.URLField("URL", unique=True)
    file_id=models.IntegerField(help_text='file_id',null=True)  
    class Meta:
        db_table='urls_information'