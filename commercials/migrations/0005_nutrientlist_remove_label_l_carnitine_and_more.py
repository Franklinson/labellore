# Generated by Django 4.2.11 on 2024-05-09 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercials', '0004_label_l_carnitine_label_l_carnitine_unit_label_mufa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NutrientList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='label',
            name='L_carnitine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='L_carnitine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='MUFA',
        ),
        migrations.RemoveField(
            model_name='label',
            name='MUFA_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='PUFA',
        ),
        migrations.RemoveField(
            model_name='label',
            name='PUFA_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='added_sugar',
        ),
        migrations.RemoveField(
            model_name='label',
            name='added_sugar_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='alanine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='alanine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='label',
            name='alcohol_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='apha_linolenic',
        ),
        migrations.RemoveField(
            model_name='label',
            name='apha_linolenic_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='arginine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='arginine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='ash',
        ),
        migrations.RemoveField(
            model_name='label',
            name='ash_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='aspartic',
        ),
        migrations.RemoveField(
            model_name='label',
            name='aspartic_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='caffeine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='caffeine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='calcium',
        ),
        migrations.RemoveField(
            model_name='label',
            name='calcium_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='carbohydrate',
        ),
        migrations.RemoveField(
            model_name='label',
            name='carbohydrate_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='carotenes',
        ),
        migrations.RemoveField(
            model_name='label',
            name='carotenes_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='casein',
        ),
        migrations.RemoveField(
            model_name='label',
            name='casein_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='chloride',
        ),
        migrations.RemoveField(
            model_name='label',
            name='chloride_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cholesterol',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cholesterol_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cholin',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cholin_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='chromium',
        ),
        migrations.RemoveField(
            model_name='label',
            name='chromium_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='copper',
        ),
        migrations.RemoveField(
            model_name='label',
            name='copper_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cystine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='cystine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='dietary_fiber',
        ),
        migrations.RemoveField(
            model_name='label',
            name='dietary_fiber_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='fat',
        ),
        migrations.RemoveField(
            model_name='label',
            name='fat_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='flouride',
        ),
        migrations.RemoveField(
            model_name='label',
            name='flouride_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='glutamic',
        ),
        migrations.RemoveField(
            model_name='label',
            name='glutamic_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='glycine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='glycine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='histidine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='histidine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='inositol',
        ),
        migrations.RemoveField(
            model_name='label',
            name='inositol_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='iodine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='iodine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='iron',
        ),
        migrations.RemoveField(
            model_name='label',
            name='iron_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='isoleucine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='isoleucine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='leucine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='leucine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='linolenic',
        ),
        migrations.RemoveField(
            model_name='label',
            name='linolenic_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='lutein',
        ),
        migrations.RemoveField(
            model_name='label',
            name='lutein_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='manganese',
        ),
        migrations.RemoveField(
            model_name='label',
            name='manganese_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='maxagnesium',
        ),
        migrations.RemoveField(
            model_name='label',
            name='maxagnesium_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='methionine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='methionine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='moisture',
        ),
        migrations.RemoveField(
            model_name='label',
            name='moisture_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='molybdenum',
        ),
        migrations.RemoveField(
            model_name='label',
            name='molybdenum_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='nucleotides',
        ),
        migrations.RemoveField(
            model_name='label',
            name='nucleotides_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='omega_3',
        ),
        migrations.RemoveField(
            model_name='label',
            name='omega_3_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='omega_6',
        ),
        migrations.RemoveField(
            model_name='label',
            name='omega_6_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='omega_9',
        ),
        migrations.RemoveField(
            model_name='label',
            name='omega_9_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='phenylalanine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='phenylalanine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='phosphorus',
        ),
        migrations.RemoveField(
            model_name='label',
            name='phosphorus_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='label',
            name='potassium_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='proline',
        ),
        migrations.RemoveField(
            model_name='label',
            name='proline_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='label',
            name='protein_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='salt',
        ),
        migrations.RemoveField(
            model_name='label',
            name='salt_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='saturated_fat',
        ),
        migrations.RemoveField(
            model_name='label',
            name='saturated_fat_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='selenium',
        ),
        migrations.RemoveField(
            model_name='label',
            name='selenium_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='serine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='serine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='label',
            name='sodium_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='sphingomyelin',
        ),
        migrations.RemoveField(
            model_name='label',
            name='sphingomyelin_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='sugar',
        ),
        migrations.RemoveField(
            model_name='label',
            name='sugar_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='taurine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='taurine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='theobromine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='theobromine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='threonine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='threonine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='trans_fat',
        ),
        migrations.RemoveField(
            model_name='label',
            name='trans_fat_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='tryptophan',
        ),
        migrations.RemoveField(
            model_name='label',
            name='tryptophan_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='tyrosine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='tyrosine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='unsaturated_fat',
        ),
        migrations.RemoveField(
            model_name='label',
            name='unsaturated_fat_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='valine',
        ),
        migrations.RemoveField(
            model_name='label',
            name='valine_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_A',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_A_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B1',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B12',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B12_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B1_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B2',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B2_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B3',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B3_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B5',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B5_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B6',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B6_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B7',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B7_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B9',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_B9_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_C',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_C_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_D',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_D_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_E',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_E_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_K',
        ),
        migrations.RemoveField(
            model_name='label',
            name='vitamin_K_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='whey',
        ),
        migrations.RemoveField(
            model_name='label',
            name='whey_unit',
        ),
        migrations.RemoveField(
            model_name='label',
            name='zinc',
        ),
        migrations.RemoveField(
            model_name='label',
            name='zinc_unit',
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, max_length=50, null=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.label')),
                ('nutrient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.nutrientlist')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.unit')),
            ],
        ),
    ]
