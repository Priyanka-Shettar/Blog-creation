# Generated by Django 2.2.1 on 2019-05-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Blog'),
        ),
    ]