# Generated by Django 4.2.1 on 2023-05-29 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0007_alter_personnel_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other'), ('N', 'Prefer Not Say')], max_length=19),
        ),
    ]
