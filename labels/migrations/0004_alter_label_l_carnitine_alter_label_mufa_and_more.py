# Generated by Django 4.2.11 on 2024-03-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_label_fat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='L_carnitine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='MUFA',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='PUFA',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='added_sugar',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='alanine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='alcoholc',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='apha_linolenic',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='arginine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='ash',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='aspartic',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='brand',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='caffeine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='calcium',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='carbohydrate',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='carotenes',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='casein',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='chloride',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='cholesterol',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='cholin',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='chromium',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='copper',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='cystine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='dietary_fiber',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='energy',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='fat',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='flouride',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='glutamic',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='glycine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='histidine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='inositol',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='iodine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='iron',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='isoleucine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='leucine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='linolenic',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='lutein',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='manganese',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='maxagnesium',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='methionine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='moisture',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='molybdenum',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='net_weight',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='nucleotides',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='omega_3',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='omega_6',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='omega_9',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='per',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='phenylalanine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='phosphorus',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='potassium',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='proline',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='protein',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='salt',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='saturated_fat',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='selenium',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='serine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='serving_quantity',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='serving_size',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='sodium',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='sphingomyelin',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='sugar',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='taurine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='theobromine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='threonine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='trans_fat',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='tryptophan',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='tyrosine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='unsaturated_fat',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='valine',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_A',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B1',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B12',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B2',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B3',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B5',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B6',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B7',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_B9',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_C',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_D',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_E',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='vitamin_K',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='whey',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='zinc',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
    ]
