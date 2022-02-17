# Generated by Django 4.0.2 on 2022-02-15 19:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_issue_resolve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='resolve',
            new_name='response',
        ),
        migrations.AddField(
            model_name='issue',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='indicator1',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='issue',
            name='indicator2',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='issue',
            name='indicator3',
            field=models.CharField(max_length=8),
        ),
    ]