# Generated by Django 4.2.5 on 2023-09-25 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_plant_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='name',
            new_name='common_name',
        ),
        migrations.AddField(
            model_name='plant',
            name='family',
            field=models.CharField(default='some plant', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='genus',
            field=models.CharField(default='some other plant', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
