# Generated by Django 4.2.10 on 2024-11-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')], default='Open', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
