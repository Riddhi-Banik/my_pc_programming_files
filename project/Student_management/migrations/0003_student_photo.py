# Generated by Django 5.1.1 on 2024-09-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_management', '0002_delete_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(default='exit', upload_to='img/%y'),
            preserve_default=False,
        ),
    ]