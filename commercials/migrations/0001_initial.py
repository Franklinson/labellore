# Generated by Django 4.2.11 on 2024-05-02 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('TINNED FOODS', 'TINNED FOODS'), ('INSTANT STAPLES', 'INSTANT STAPLES'), ('DAIRY & CREAMERS', 'DAIRY & CREAMERS'), ('OILS', 'OILS'), ('BISCUITS', 'BISCUITS'), ('BEVERAGES', 'BEVERAGES'), ('SPREADS, DRESSINGS & SAUCES', ' SPREADS, DRESSINGS & SAUCES'), ('GRAINS & CEREALS', 'GRAINS & CEREALS'), ('PASTA', 'PASTA'), ('INFANT FORMULAE', 'INFANT FORMULAE'), ('NUTRITION SUPPLEMENTS', 'NUTRITION SUPPLEMENTS'), ('SPICES', 'SPICES')], max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('net_weight', models.FloatField(blank=True, max_length=50, null=True)),
                ('serving_size', models.FloatField(blank=True, max_length=50, null=True)),
                ('serving_quantity', models.FloatField(blank=True, max_length=50, null=True)),
                ('per', models.FloatField(blank=True, max_length=50, null=True)),
                ('energy', models.FloatField(blank=True, max_length=50, null=True)),
                ('carbohydrate', models.FloatField(blank=True, max_length=50, null=True)),
                ('protein', models.FloatField(blank=True, max_length=50, null=True)),
                ('sugar', models.FloatField(blank=True, max_length=50, null=True)),
                ('added_sugar', models.FloatField(blank=True, max_length=50, null=True)),
                ('fat', models.FloatField(blank=True, max_length=50, null=True)),
                ('PUFA', models.FloatField(blank=True, max_length=50, null=True)),
                ('MUFA', models.FloatField(blank=True, max_length=50, null=True)),
                ('omega_3', models.FloatField(blank=True, max_length=50, null=True)),
                ('omega_6', models.FloatField(blank=True, max_length=50, null=True)),
                ('omega_9', models.FloatField(blank=True, max_length=50, null=True)),
                ('saturated_fat', models.FloatField(blank=True, max_length=50, null=True)),
                ('unsaturated_fat', models.FloatField(blank=True, max_length=50, null=True)),
                ('trans_fat', models.FloatField(blank=True, max_length=50, null=True)),
                ('dietary_fiber', models.FloatField(blank=True, max_length=50, null=True)),
                ('sodium', models.FloatField(blank=True, max_length=50, null=True)),
                ('salt', models.FloatField(blank=True, max_length=50, null=True)),
                ('potassium', models.FloatField(blank=True, max_length=50, null=True)),
                ('iron', models.FloatField(blank=True, max_length=50, null=True)),
                ('cholesterol', models.FloatField(blank=True, max_length=50, null=True)),
                ('calcium', models.FloatField(blank=True, max_length=50, null=True)),
                ('maxagnesium', models.FloatField(blank=True, max_length=50, null=True)),
                ('phosphorus', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_A', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B1', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B2', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B3', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B5', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B6', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B7', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B9', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_B12', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_C', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_D', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_E', models.FloatField(blank=True, max_length=50, null=True)),
                ('vitamin_K', models.FloatField(blank=True, max_length=50, null=True)),
                ('iodine', models.FloatField(blank=True, max_length=50, null=True)),
                ('zinc', models.FloatField(blank=True, max_length=50, null=True)),
                ('chloride', models.FloatField(blank=True, max_length=50, null=True)),
                ('manganese', models.FloatField(blank=True, max_length=50, null=True)),
                ('selenium', models.FloatField(blank=True, max_length=50, null=True)),
                ('molybdenum', models.FloatField(blank=True, max_length=50, null=True)),
                ('flouride', models.FloatField(blank=True, max_length=50, null=True)),
                ('chromium', models.FloatField(blank=True, max_length=50, null=True)),
                ('copper', models.FloatField(blank=True, max_length=50, null=True)),
                ('casein', models.FloatField(blank=True, max_length=50, null=True)),
                ('ash', models.FloatField(blank=True, max_length=50, null=True)),
                ('linolenic', models.FloatField(blank=True, max_length=50, null=True)),
                ('apha_linolenic', models.FloatField(blank=True, max_length=50, null=True)),
                ('moisture', models.FloatField(blank=True, max_length=50, null=True)),
                ('cholin', models.FloatField(blank=True, max_length=50, null=True)),
                ('inositol', models.FloatField(blank=True, max_length=50, null=True)),
                ('taurine', models.FloatField(blank=True, max_length=50, null=True)),
                ('L_carnitine', models.FloatField(blank=True, max_length=50, null=True)),
                ('nucleotides', models.FloatField(blank=True, max_length=50, null=True)),
                ('sphingomyelin', models.FloatField(blank=True, max_length=50, null=True)),
                ('lutein', models.FloatField(blank=True, max_length=50, null=True)),
                ('carotenes', models.FloatField(blank=True, max_length=50, null=True)),
                ('whey', models.FloatField(blank=True, max_length=50, null=True)),
                ('tryptophan', models.FloatField(blank=True, max_length=50, null=True)),
                ('threonine', models.FloatField(blank=True, max_length=50, null=True)),
                ('isoleucine', models.FloatField(blank=True, max_length=50, null=True)),
                ('leucine', models.FloatField(blank=True, max_length=50, null=True)),
                ('methionine', models.FloatField(blank=True, max_length=50, null=True)),
                ('cystine', models.FloatField(blank=True, max_length=50, null=True)),
                ('phenylalanine', models.FloatField(blank=True, max_length=50, null=True)),
                ('tyrosine', models.FloatField(blank=True, max_length=50, null=True)),
                ('valine', models.FloatField(blank=True, max_length=50, null=True)),
                ('arginine', models.FloatField(blank=True, max_length=50, null=True)),
                ('histidine', models.FloatField(blank=True, max_length=50, null=True)),
                ('alanine', models.FloatField(blank=True, max_length=50, null=True)),
                ('aspartic', models.FloatField(blank=True, max_length=50, null=True)),
                ('glutamic', models.FloatField(blank=True, max_length=50, null=True)),
                ('glycine', models.FloatField(blank=True, max_length=50, null=True)),
                ('proline', models.FloatField(blank=True, max_length=50, null=True)),
                ('serine', models.FloatField(blank=True, max_length=50, null=True)),
                ('alcohol', models.FloatField(blank=True, max_length=50, null=True)),
                ('caffeine', models.FloatField(blank=True, max_length=50, null=True)),
                ('theobromine', models.FloatField(blank=True, max_length=50, null=True)),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.category')),
                ('L_carnitine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='L_carnitine_unit', to='commercials.unit')),
                ('MUFA_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MUFA_unit', to='commercials.unit')),
                ('PUFA_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PUFA_unit', to='commercials.unit')),
                ('added_sugar_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_sugar_unit', to='commercials.unit')),
                ('alanine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alanine_unit', to='commercials.unit')),
                ('alcohol_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alcohol_unit', to='commercials.unit')),
                ('apha_linolenic_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apha_linolenic_unit', to='commercials.unit')),
                ('arginine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arginine_unit', to='commercials.unit')),
                ('ash_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ash_unit', to='commercials.unit')),
                ('aspartic_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aspartic_unit', to='commercials.unit')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commercials.brand')),
                ('caffeine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caffeine_unit', to='commercials.unit')),
                ('calcium_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calcium_unit', to='commercials.unit')),
                ('carbohydrate_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carbohydrate_unit', to='commercials.unit')),
                ('carotenes_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carotenes_unit', to='commercials.unit')),
                ('casein_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='casein_unit', to='commercials.unit')),
                ('chloride_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chloride_unit', to='commercials.unit')),
                ('cholesterol_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cholesterol_unit', to='commercials.unit')),
                ('cholin_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cholin_unit', to='commercials.unit')),
                ('chromium_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chromium_unit', to='commercials.unit')),
                ('copper_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='copper_unit', to='commercials.unit')),
                ('cystine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cystine_unit', to='commercials.unit')),
                ('dietary_fiber_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dietary_fiber_unit', to='commercials.unit')),
                ('energy_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='energy_unit', to='commercials.unit')),
                ('fat_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fat_unit', to='commercials.unit')),
                ('flouride_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flouride_unit', to='commercials.unit')),
                ('glutamic_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='glutamic_unit', to='commercials.unit')),
                ('glycine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='glycine_unit', to='commercials.unit')),
                ('histidine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='histidine_unit', to='commercials.unit')),
                ('inositol_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inositol_unit', to='commercials.unit')),
                ('iodine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='iodine_unit', to='commercials.unit')),
                ('iron_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='iron_unit', to='commercials.unit')),
                ('isoleucine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='isoleucine_unit', to='commercials.unit')),
                ('leucine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leucine_unit', to='commercials.unit')),
                ('linolenic_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linolenic_unit', to='commercials.unit')),
                ('lutein_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lutein_unit', to='commercials.unit')),
                ('manganese_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manganese_unit', to='commercials.unit')),
                ('maxagnesium_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maxagnesium_unit', to='commercials.unit')),
                ('methionine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='methionine_unit', to='commercials.unit')),
                ('moisture_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moisture_unit', to='commercials.unit')),
                ('molybdenum_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='molybdenum_unit', to='commercials.unit')),
                ('net_weight_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='net_weight_unit', to='commercials.unit')),
                ('nucleotides_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nucleotides_unit', to='commercials.unit')),
                ('omega_3_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='omega_3_unit', to='commercials.unit')),
                ('omega_6_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='omega_6_unit', to='commercials.unit')),
                ('omega_9_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='omega_9_unit', to='commercials.unit')),
                ('per_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='per_unit', to='commercials.unit')),
                ('phenylalanine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phenylalanine_unit', to='commercials.unit')),
                ('phosphorus_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phosphorus_unit', to='commercials.unit')),
                ('potassium_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='potassium_unit', to='commercials.unit')),
                ('proline_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proline_unit', to='commercials.unit')),
                ('protein_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='protein_unit', to='commercials.unit')),
                ('salt_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salt_unit', to='commercials.unit')),
                ('saturated_fat_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='saturated_fat_unit', to='commercials.unit')),
                ('selenium_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='selenium_unit', to='commercials.unit')),
                ('serine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serine_unit', to='commercials.unit')),
                ('serving_quantity_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serving_quantity_unit', to='commercials.unit')),
                ('serving_size_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serving_size_unit', to='commercials.unit')),
                ('sodium_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sodium_unit', to='commercials.unit')),
                ('sphingomyelin_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sphingomyelin_unit', to='commercials.unit')),
                ('sugar_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sugar_unit', to='commercials.unit')),
                ('taurine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taurine_unit', to='commercials.unit')),
                ('theobromine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='theobromine_unit', to='commercials.unit')),
                ('threonine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='threonine_unit', to='commercials.unit')),
                ('trans_fat_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trans_fat_unit', to='commercials.unit')),
                ('tryptophan_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tryptophan_unit', to='commercials.unit')),
                ('tyrosine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tyrosine_unit', to='commercials.unit')),
                ('unsaturated_fat_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unsaturated_fat_unit', to='commercials.unit')),
                ('valine_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='valine_unit', to='commercials.unit')),
                ('vitamin_A_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_A_unit', to='commercials.unit')),
                ('vitamin_B12_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B12_unit', to='commercials.unit')),
                ('vitamin_B1_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B1_unit', to='commercials.unit')),
                ('vitamin_B2_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B2_unit', to='commercials.unit')),
                ('vitamin_B3_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B3_unit', to='commercials.unit')),
                ('vitamin_B5_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B5_unit', to='commercials.unit')),
                ('vitamin_B6_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B6_unit', to='commercials.unit')),
                ('vitamin_B7_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B7_unit', to='commercials.unit')),
                ('vitamin_B9_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_B9_unit', to='commercials.unit')),
                ('vitamin_C_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_C_unit', to='commercials.unit')),
                ('vitamin_D_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_D_unit', to='commercials.unit')),
                ('vitamin_E_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_E_unit', to='commercials.unit')),
                ('vitamin_K_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vitamin_K_unit', to='commercials.unit')),
                ('whey_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='whey_unit', to='commercials.unit')),
                ('zinc_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zinc_unit', to='commercials.unit')),
            ],
        ),
    ]
