# Generated by Django 4.2.11 on 2024-03-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0004_alter_label_l_carnitine_alter_label_mufa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='categories',
            field=models.CharField(choices=[('TINNED FOODS', 'TINNED FOODS'), ('INSTANT STAPLES', 'INSTANT STAPLES'), ('DAIRY & CREAMERS', 'DAIRY & CREAMERS'), ('OILS', 'OILS'), ('BISCUITS', 'BISCUITS'), ('BEVEARAGES', 'BEVERAGES'), ('SPREADS, DRESSINGS & SAUCES', ' SPREADS, DRESSINGS & SAUCES'), ('GRAINS & CEREALS', 'GRAINS & CEREALS'), ('PASTA', 'PASTA'), ('INFANT FORMULAE', 'INFANT FORMULAE'), ('NUTRITION SUPPLEMENTS', 'NUTRITION SUPPLEMENTS'), ('SPICES', 'SPICES')], max_length=100),
        ),
    ]
