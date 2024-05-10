# Generated by Django 4.2.11 on 2024-05-09 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercials', '0005_nutrientlist_remove_label_l_carnitine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='nutrient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.nutrientlist'),
        ),
        migrations.AddField(
            model_name='label',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commercials.label'),
        ),
        migrations.AddField(
            model_name='label',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.unit'),
        ),
        migrations.AddField(
            model_name='label',
            name='value',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Nutrient',
        ),
    ]
