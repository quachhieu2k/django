# Generated by Django 4.0.5 on 2022-07-07 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8_general_ci', max_length=100, null=True)),
                ('teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=45, null=True)),
                ('is_finished', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblCourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_collation='utf8_general_ci', max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('thumbnail', models.ImageField(upload_to='images/')),
                ('link_video_ytb', models.CharField(blank=True, max_length=50, null=True)),
                ('is_finished', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.tblcourse')),
            ],
        ),
    ]
