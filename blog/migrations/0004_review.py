# Generated by Django 4.2.11 on 2024-03-19 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('date_review', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('approved', models.BooleanField(default=False)),
                ('author_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
                ('post_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.post')),
            ],
        ),
    ]
