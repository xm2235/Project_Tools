# Generated by Django 3.0.6 on 2020-05-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20200511_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, default=None, max_digits=50, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=10, default=None, max_digits=50, verbose_name='Longitude')),
                ('unique_squirrel_id', models.CharField(default=None, max_length=50, verbose_name='ID')),
                ('shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default=None, max_length=50, verbose_name='Shift')),
                ('date', models.DateField(default=None, max_length=50, verbose_name='Date')),
                ('age', models.CharField(choices=[('Juvenile', 'Juvenile'), ('Adult', 'Adult'), ('None', 'None')], default=None, max_length=50, verbose_name='Age')),
                ('color', models.CharField(choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon')], default=None, max_length=50, verbose_name='Color')),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('None', 'None')], default=None, max_length=50, verbose_name='Location')),
                ('specific_location', models.CharField(default=None, max_length=50, verbose_name='Specific_location')),
                ('running', models.BooleanField(default=False, verbose_name='Running')),
                ('chasing', models.BooleanField(default=False, verbose_name='Chasing')),
                ('climbing', models.BooleanField(default=False, verbose_name='Climbing')),
                ('eating', models.BooleanField(default=False, verbose_name='Eating')),
                ('foraging', models.BooleanField(default=False, verbose_name='Foraging')),
                ('other_activity', models.CharField(default=None, max_length=50, verbose_name='Other_activity')),
                ('kuks', models.BooleanField(default=False, verbose_name='Kuks')),
                ('quaas', models.BooleanField(default=False, verbose_name='Quaas')),
                ('moans', models.BooleanField(default=False, verbose_name='Moans')),
                ('tail_flags', models.BooleanField(default=False, verbose_name='Tail_flags')),
                ('tail_twitches', models.BooleanField(default=False, verbose_name='Tail_twitches')),
                ('approaches', models.BooleanField(default=False, verbose_name='Approaches')),
                ('indifferent', models.BooleanField(default=False, verbose_name='Indifferent')),
                ('runs_from', models.BooleanField(default=False, verbose_name='Runs_from')),
            ],
        ),
        migrations.DeleteModel(
            name='squirrel',
        ),
    ]
