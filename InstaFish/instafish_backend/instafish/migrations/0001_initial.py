# Generated by Django 2.2 on 2019-06-04 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import instafish.models
import instafish.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Mężczyzna'), ('Female', 'Kobieta')], max_length=20, null=True)),
                ('birthdate', models.DateField(blank=True, null=True, validators=[instafish.validators.validate_date_not_in_future])),
                ('country', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('specialization', models.CharField(blank=True, default='brak', max_length=200)),
                ('organization', models.CharField(blank=True, default='brak', max_length=200)),
                ('avatar', models.ImageField(default='fish.jpg', upload_to=instafish.models.upload_to, validators=[instafish.validators.validate_file_size])),
                ('communities', models.BooleanField(default=True)),
                ('facebook', models.CharField(blank=True, max_length=200)),
                ('instagram', models.CharField(blank=True, max_length=200)),
                ('youtube', models.CharField(blank=True, max_length=200)),
                ('website', models.CharField(blank=True, max_length=200)),
                ('fishing_rod', models.CharField(blank=True, default='brak', max_length=200)),
                ('fishing_reel', models.CharField(blank=True, default='brak', max_length=200)),
                ('achievement', models.CharField(blank=True, default='brak', max_length=200)),
                ('description', models.CharField(blank=True, default='brak', max_length=1000)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='instafish.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.datetime_safe.datetime.utcnow, editable=False)),
                ('title', models.CharField(max_length=64)),
                ('fish_name', models.CharField(blank=True, max_length=200, null=True)),
                ('fish_weight', models.CharField(blank=True, max_length=200, null=True)),
                ('fish_length', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_country', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_city', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_date', models.DateField()),
                ('fish_photo', models.ImageField(upload_to='posts/', validators=[instafish.validators.validate_file_size])),
                ('fishing_reel', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_leader', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_hook', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_rod', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_bait', models.CharField(blank=True, max_length=200, null=True)),
                ('fishing_line', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('hashtag', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('localization', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.datetime_safe.datetime.utcnow, editable=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('yes', 'Wezmę udział'), ('no', 'Nie wezmę udziału'), ('idk', 'Niezdecydowany')], max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Profile')),
            ],
            options={
                'unique_together': {('user', 'event')},
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLiked', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instafish.Profile')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
    ]