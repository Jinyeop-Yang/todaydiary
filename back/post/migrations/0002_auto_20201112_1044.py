<<<<<<< HEAD:back/post/migrations/0002_auto_20201112_1535.py
# Generated by Django 2.2.15 on 2020-11-12 06:35
=======
# Generated by Django 2.2.15 on 2020-11-12 01:44
>>>>>>> 4f538dbc968b2582c30662df527dc73b579aba9c:back/post/migrations/0002_auto_20201112_1044.py

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD:back/post/migrations/0002_auto_20201112_1535.py
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('text', '0001_initial'),
        ('post', '0001_initial'),
=======
        ('post', '0001_initial'),
        ('text', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> 4f538dbc968b2582c30662df527dc73b579aba9c:back/post/migrations/0002_auto_20201112_1044.py
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='text.DailyReport'),
        ),
        migrations.AddField(
            model_name='post',
            name='search_music',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='search_music', to='post.SearchMusic'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='user_emotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.Emotion'),
        ),
    ]
