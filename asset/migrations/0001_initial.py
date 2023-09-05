# Generated by Django 4.2.2 on 2023-09-05 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "serial_number",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("asset_type", models.CharField(max_length=50)),
                ("model_type", models.CharField(max_length=50)),
                ("model_number", models.CharField(max_length=50)),
                ("mac_address", models.CharField(max_length=50)),
                ("os", models.BooleanField(default=False, max_length=50)),
                ("wake_on_lan", models.BooleanField(default=False, max_length=50)),
                ("kav", models.BooleanField(default=False, max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[("Working", "Working"), ("Faulty", "Faulty")],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Division",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("DEPUTY COMMISIONNER", "8"),
                            ("CHIEF MANAGER", "7"),
                            ("MANAGER", "6"),
                            ("ASSISTANT MANAGER", "5"),
                            ("SUPERVISER", "4"),
                            ("OFFICER", "3"),
                            ("SUPPORT II", "2"),
                            ("SUPPORT I", "1"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.division"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Station",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "personal_number",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("domain", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("role", models.CharField(max_length=50)),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.section"
                    ),
                ),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.station"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "ticket_number",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "ict_officer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="asset.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "staff_number",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("staff_name", models.CharField(max_length=50)),
                ("designation", models.CharField(max_length=50)),
                ("grade", models.CharField(max_length=50)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset.department",
                    ),
                ),
                (
                    "division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.division"
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.section"
                    ),
                ),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.station"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeployedAsset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("previous_location", models.CharField(max_length=50)),
                ("current_location", models.CharField(max_length=50)),
                (
                    "movement_form",
                    models.FileField(default=None, upload_to="scanned_forms/"),
                ),
                (
                    "movement_type",
                    models.CharField(
                        choices=[
                            ("NEW DEPLOYEMENT", "NEW DEPLOYEMENT"),
                            ("REDEPLOYMENT", "REDEPLOYEMENT"),
                            ("REDEPLOYMENT", "RE-LOCATION"),
                            ("CHANGE OF OWNERSHIP", "CHANGE OF OWNERSHIP"),
                            ("SURRENDER", "SURRENDER"),
                            ("EXIT WITH", "EXIT WITH"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="asset.asset"
                    ),
                ),
                (
                    "current_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="current_user",
                        to="asset.user",
                    ),
                ),
                (
                    "previous_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="previous_user",
                        to="asset.user",
                    ),
                ),
                (
                    "workticket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="asset.ticket"
                    ),
                ),
            ],
        ),
    ]
