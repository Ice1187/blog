# Generated by Django 2.2.4 on 2019-08-26 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190827_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteupTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='writeuparticle',
            name='tags',
        ),
        migrations.AddField(
            model_name='writeuparticle',
            name='tags',
            field=models.ManyToManyField(to='blog.WriteupTag'),
        ),
    ]
