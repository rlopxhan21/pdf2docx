# Generated by Django 4.1.7 on 2023-03-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file', models.FileField(upload_to='uploaded_file/')),
                ('converted_file', models.FileField(blank=True, null=True, upload_to='converted_file/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]