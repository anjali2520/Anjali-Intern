

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_remove_issuedbook_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
