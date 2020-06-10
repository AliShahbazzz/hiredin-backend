# Generated by Django 2.2 on 2020-06-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20200608_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresume',
            name='project_role_1',
        ),
        migrations.RemoveField(
            model_name='userresume',
            name='project_role_2',
        ),
        migrations.RemoveField(
            model_name='userresume',
            name='project_role_3',
        ),
        migrations.AddField(
            model_name='userresume',
            name='project_description_1',
            field=models.TextField(blank=True, help_text='Decsribe Project', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userresume',
            name='project_description_2',
            field=models.TextField(blank=True, help_text='Describe Project', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userresume',
            name='project_description_3',
            field=models.TextField(blank=True, help_text='Describe Project', max_length=300, null=True),
        ),
    ]