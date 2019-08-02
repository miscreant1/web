# Generated by Django 2.2.3 on 2019-07-31 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0025_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='request_ownership_change',
            field=models.ForeignKey(blank=True, help_text="The Grant's potential new administrator profile.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_ownership_change', to='dashboard.Profile'),
        ),
    ]