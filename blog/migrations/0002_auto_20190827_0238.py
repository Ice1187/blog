# Generated by Django 2.2.4 on 2019-08-26 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteupCTF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknow', max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='writeuparticle',
            name='date',
        ),
        migrations.AlterField(
            model_name='writeuparticle',
            name='ctf',
            field=models.ForeignKey(default='Unknow', on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.WriteupCTF'),
        ),
    ]