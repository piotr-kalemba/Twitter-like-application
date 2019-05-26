# Generated by Django 2.2 on 2019-05-24 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20190524_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=60)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Tweet')),
            ],
        ),
    ]
