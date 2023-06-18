# Generated by Django 4.2.1 on 2023-05-29 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_alter_personnel_gender_alter_personnel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other'), ('N', 'Prefer Not Say')], max_length=19),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='title',
            field=models.CharField(choices=[('S', 'Senior'), ('M', 'Mid Senior'), ('J', 'Junior')], max_length=15),
        ),
    ]