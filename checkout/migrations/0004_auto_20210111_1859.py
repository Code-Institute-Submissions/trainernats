# Generated by Django 3.1.2 on 2021-01-11 05:59

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
        ('checkout', '0003_auto_20210111_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='memberships.usermembership'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]