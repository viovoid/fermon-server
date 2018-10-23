# Generated by Django 2.1.1 on 2018-10-23 03:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='brew',
            name='ident',
            field=models.CharField(max_length=32),
        ),
        migrations.AddField(
            model_name='update',
            name='brew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brews.Brew'),
        ),
    ]
