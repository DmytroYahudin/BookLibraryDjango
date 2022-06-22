# Generated by Django 4.0.3 on 2022-03-23 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='for_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre', null=True, to='catalog.genre'),
        ),
    ]
