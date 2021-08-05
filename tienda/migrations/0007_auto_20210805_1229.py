# Generated by Django 3.2.5 on 2021-08-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img',
            field=models.CharField(default='fotito', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='BASE_DIR/staticfiles/tienda/img'),
        ),
    ]