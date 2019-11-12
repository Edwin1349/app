# Generated by Django 2.2.6 on 2019-11-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hello', '0006_auto_20191103_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='people', to='Hello.Family')),
            ],
            options={
                'unique_together': {('password',)},
            },
        ),
        migrations.RemoveField(
            model_name='budget',
            name='users',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hello.User'),
        ),
    ]