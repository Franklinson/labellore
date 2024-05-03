# Generated by Django 4.2.11 on 2024-05-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Locals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='Category',
        ),
        migrations.AddField(
            model_name='label',
            name='categories',
            field=models.CharField(blank=True, choices=[('ANIMAL PROTEINS', 'ANIMAL PROTEINS '), ('SOUP AND STEWS', 'SOUP AND STEWS'), ('PORRIDGES', 'PORRIDGES'), ('LOCAL STAPLES', 'LOCAL STAPLES'), ('FRUITS AND VEGETABLES', 'FRUITS AND VEGETABLES'), ('NUTS AND LEGUMES', 'NUTS AND LEGUMES')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
