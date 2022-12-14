# Generated by Django 4.1.1 on 2022-09-12 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_route_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=None)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
    ]
