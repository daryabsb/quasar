# Generated by Django 4.1.5 on 2023-01-18 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_title_appointment_treatment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skeletal_class', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('nasolabial_angle', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='normal', max_length=200)),
                ('nasolabial_sulcus', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='normal', max_length=200)),
                ('overjet', models.CharField(default='Diskjet', max_length=60)),
                ('oral_hygiene', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='good', max_length=200)),
                ('lip_competency', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='competent', max_length=200)),
                ('face_form', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='dolichocephalic', max_length=200)),
                ('habit', models.CharField(default='Naughty', max_length=60)),
                ('treated_arch', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='max', max_length=200)),
                ('molar_class_left', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('molar_class_right', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('tongue_size', models.CharField(default='Long', max_length=60)),
                ('bracket_system', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('midline_upper', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='coincidence', max_length=200)),
                ('midline_lower', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='coincidence', max_length=200)),
                ('slot', models.CharField(default='normal', max_length=60)),
                ('extraction_upper', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('extraction_lower', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('anchorage_upper', models.CharField(choices=[('class1', 'CLASS I'), ('class2', 'CLASS II'), ('class3', 'CLASS III'), ('normal', 'NORMAL'), ('acute', 'ACUTE'), ('obtuse', 'OBTUCE'), ('deep', 'DEEP'), ('competent', 'COMPETENT'), ('incompetent', 'INCOMPETENT'), ('partially_competent', 'PARTIALLY_COMPETENT'), ('dolichocephalic', 'DOLICHOCEPHALIC'), ('mesocephalic', 'MESOCEPHALIC'), ('brachycephalic', 'BRACHYCEPHALIC'), ('coincidence', 'COINIDENCE'), ('deviated_to_left', 'DEVIATED TO LEFT'), ('deviated_to_right', 'DEVIATED TO RIGHT'), ('good', 'GOOD'), ('fair', 'FAIR'), ('bad', 'BAD'), ('max', 'MAX'), ('mand', 'MAND')], default='class1', max_length=200)),
                ('treatment_plan', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='examinations', to='core.client')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
