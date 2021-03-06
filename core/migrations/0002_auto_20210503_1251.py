# Generated by Django 3.1.7 on 2021-05-03 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_bell',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.bell'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_ring',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.ring'),
        ),
    ]
