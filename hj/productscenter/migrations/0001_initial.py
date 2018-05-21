# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_text', models.CharField(max_length=50)),
                ('opdate', models.DateTimeField(auto_now=True)),
                ('delflag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AgentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opdate', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='AgentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenttype_text', models.CharField(max_length=20)),
                ('opdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park_text', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=100)),
                ('opdate', models.DateTimeField(auto_now=True)),
                ('delflag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_text', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('saleflag', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=100)),
                ('opdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productproperty_text', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=100)),
                ('opdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype_text', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=100)),
                ('opdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminal_text', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=50)),
                ('delflag', models.BooleanField(default=False)),
                ('opdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='productproperty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.ProductProperty'),
        ),
        migrations.AddField(
            model_name='product',
            name='producttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.ProductType'),
        ),
        migrations.AddField(
            model_name='agentproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.Product'),
        ),
        migrations.AddField(
            model_name='agent',
            name='agenttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.AgentType'),
        ),
        migrations.AddField(
            model_name='accesspark',
            name='park',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.Park'),
        ),
        migrations.AddField(
            model_name='accesspark',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productscenter.Product'),
        ),
    ]
