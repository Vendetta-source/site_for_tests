# Generated by Django 4.1.1 on 2022-09-17 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestsBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название теста', max_length=200, verbose_name='Название теста')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=1000)),
                ('test', models.ForeignKey(help_text='Выберите тест', on_delete=django.db.models.deletion.CASCADE, to='tests.testsbase')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True, help_text='Введите ответ на вопрос', max_length=1000, verbose_name='Ответ на вопрос')),
                ('answer_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Ответ на вопрос изображением')),
                ('correct_answer', models.BooleanField(blank=True, default=False)),
                ('question', models.ForeignKey(help_text='Выберите вопрос', on_delete=django.db.models.deletion.CASCADE, to='tests.questions')),
            ],
        ),
    ]
