# Generated by Django 2.2.4 on 2019-11-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191117_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'get_latest_by': 'product_published_date', 'ordering': ['product_cost'], 'verbose_name_plural': 'ProductVS'},
        ),
        migrations.AlterField(
            model_name='products',
            name='product_size_choices',
            field=models.CharField(choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L')], max_length=20),
        ),
        migrations.AlterModelTable(
            name='products',
            table='products_products',
        ),
    ]
