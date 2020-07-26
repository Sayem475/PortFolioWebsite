# Generated by Django 3.0.6 on 2020-07-23 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.CreateModel(
            name='PortfolioImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('portfolio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.Portfolio')),
            ],
        ),
    ]
