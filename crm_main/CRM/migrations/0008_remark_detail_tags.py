# Generated by Django 4.0.3 on 2022-04-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0007_query1_customer_query1_query_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='detail',
            name='tags',
            field=models.ManyToManyField(to='CRM.remark'),
        ),
    ]