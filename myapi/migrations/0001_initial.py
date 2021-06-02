# Generated by Django 3.2.3 on 2021-06-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('department', models.CharField(max_length=60)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]