# Generated by Django 2.2.12 on 2020-09-02 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200818_0723'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostCategory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_category',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_category',
        ),
        migrations.DeleteModel(
            name='WorkCategory',
        ),
    ]