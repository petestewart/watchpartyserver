# Generated by Django 3.1.4 on 2021-01-03 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchpartyserverapi', '0006_party_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='datetime_end',
            field=models.DateTimeField(default='2021-01-31 12:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='party',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='watchpartyserverapi.channel'),
        ),
    ]
