# Generated by Django 3.1.2 on 2021-01-16 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tnsclasses', '0010_class_type_friendly_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tns_class',
            name='class_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tnsclasses.class_time'),
        ),
    ]