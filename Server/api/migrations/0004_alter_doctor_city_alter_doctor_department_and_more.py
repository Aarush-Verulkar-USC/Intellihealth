# Generated by Django 4.0.2 on 2022-02-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_dateoj_doctor_doj_rename_docid_doctor_docid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
