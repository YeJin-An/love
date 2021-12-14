# Generated by Django 3.2.10 on 2021-12-14 00:35

from django.db import migrations, models
import django.db.models.deletion

def create_dummy_category(apps, schema_editor):
    Category = apps.get_model("shop","Category")
    Category.objects.create(name = "dummy")

def delete_dummy_category(apps, schema_editor):
    Category = apps.get_model("shop","Category")
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creadted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='shop.Tag'),
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.category'),
            preserve_default=False,
        ),
    ]
