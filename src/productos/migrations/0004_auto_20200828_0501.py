# Generated by Django 3.0.8 on 2020-08-28 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20200826_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='required_date',
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Customers')),
                ('employees_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Employees')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Orders')),
            ],
        ),
    ]
