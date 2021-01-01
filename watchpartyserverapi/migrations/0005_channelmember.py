# Generated by Django 3.1.4 on 2021-01-01 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchpartyserverapi', '0004_channel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchpartyserverapi.channel')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchpartyserverapi.member')),
            ],
        ),
    ]