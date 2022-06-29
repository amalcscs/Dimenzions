# Generated by Django 4.0 on 2022-03-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_register',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(default='', max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('joining_date', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('designation', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='categories',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('category_logo', models.ImageField(default='default.png', upload_to='images')),
                ('sub_category1', models.CharField(max_length=255)),
                ('sub_category2', models.CharField(max_length=255)),
                ('sub_category3', models.EmailField(max_length=255)),
                ('sub_category4', models.CharField(max_length=255)),
                ('sub_category5', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelname', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255)),
                ('gib', models.FileField(blank=True, null=True, upload_to='images/')),
                ('price', models.CharField(max_length=255)),
                ('types', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=255)),
                ('modeltype', models.CharField(max_length=255)),
                ('fbx', models.ImageField(default='default.png', upload_to='images')),
                ('cat_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.categories')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=225, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('modelname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pay_model', to='myapp.items')),
                ('price', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pay_price', to='myapp.items')),
            ],
        ),
    ]
