# Generated by Django 2.2.16 on 2022-04-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20220423_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='posts.Comment'),
        ),
    ]
