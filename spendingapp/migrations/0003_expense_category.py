# Generated by Django 5.0.2 on 2024-03-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spendingapp', '0002_expense_icon_expense_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.TextField(default='Groceries'),
            preserve_default=False,
        ),
    ]
