# Generated by Django 4.2.11 on 2024-05-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stocks", "0002_rename_price_stock_close_price_remove_stock_name_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="stock",
            unique_together={("symbol", "date")},
        ),
        migrations.AddIndex(
            model_name="stock",
            index=models.Index(
                fields=["symbol", "date"], name="stocks_stoc_symbol_ef6299_idx"
            ),
        ),
    ]
