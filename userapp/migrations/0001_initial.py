# Generated by Django 3.2.16 on 2024-06-18 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ipaddress',
            fields=[
                ('ipaddress_id', models.AutoField(primary_key=True, serialize=False)),
                ('ipaddress', models.CharField(help_text='ipaddress', max_length=200, null=True)),
                ('ipaddress_date', models.DateField(auto_now_add=True, null=True)),
                ('ipaddress_time', models.TimeField(auto_now_add=True, null=True)),
                ('existed_ipaddress_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('existed_ip_count', models.BigIntegerField(default=0, help_text='existed_ip_count')),
            ],
            options={
                'db_table': 'ipaddress',
            },
        ),
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(help_text='file_name', max_length=50, null=True)),
                ('file_password', models.CharField(help_text='file_password', max_length=50, null=True)),
                ('upload_files', models.FileField(help_text='upload_files', null=True, upload_to='')),
                ('file_size', models.CharField(help_text='file_size', max_length=50, null=True)),
                ('public_key', models.CharField(help_text='public_key', max_length=5000, null=True)),
                ('private_key', models.CharField(help_text='private_key', max_length=5000, null=True)),
                ('encrypted_key', models.CharField(help_text='encrypted_key', max_length=5000, null=True)),
                ('discribtion', models.TextField(help_text='discribtion', null=True)),
                ('self_download', models.BigIntegerField(default=0, help_text='self_download', null=True)),
                ('users_download', models.BigIntegerField(default=0, help_text='users_download', null=True)),
                ('url_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.short_urlss')),
            ],
            options={
                'db_table': 'UploadFiles',
            },
        ),
        migrations.CreateModel(
            name='UserRegisration',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('profile_photo', models.ImageField(null=True, upload_to='images/')),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(default='Accepted', max_length=500, null=True)),
                ('sum_self_download', models.BigIntegerField(default=0, help_text='sum_self_download')),
                ('no_uploads', models.BigIntegerField(default=0, help_text='no_uploads')),
                ('upload_file_size', models.BigIntegerField(default=0, help_text='no_uploads')),
                ('public_downloads', models.BigIntegerField(default=0, help_text='public_downloads')),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
        migrations.CreateModel(
            name='user_key_uploaded',
            fields=[
                ('fileno', models.AutoField(primary_key=True, serialize=False)),
                ('privatekeyfile', models.FileField(help_text='privatekeyfile', null=True, upload_to='uploadedkey')),
                ('decrypted_key', models.CharField(help_text='decrypted_key', max_length=5000, null=True)),
                ('UploadFiles', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.uploadfiles')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userregisration')),
            ],
            options={
                'db_table': 'privatekey_Uploaded_details',
            },
        ),
        migrations.AddField(
            model_name='uploadfiles',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.userregisration'),
        ),
    ]
