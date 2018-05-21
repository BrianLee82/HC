# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import datetime
#from datetime import datetime
# Create your models here.


# 产品类型(单、联)
@python_2_unicode_compatible  # 如果你需要支持Python 2
class ProductType(models.Model):
    producttype_text = models.CharField(max_length=20)
    comment = models.CharField(max_length=100)
    opdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producttype_text


# 票性质（成人、学生、教师、老人、军人)
@python_2_unicode_compatible  # 如果你需要支持Python 2
class ProductProperty(models.Model):
    productproperty_text = models.CharField(max_length=20)
    comment = models.CharField(max_length=100)
    opdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productproperty_text


@python_2_unicode_compatible  # 如果你需要支持Python 2
class Product(models.Model):
    product_text = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    saleflag = models.BooleanField(default=True)
    comment = models.CharField(max_length=100)
    opdate = models.DateTimeField(auto_now=True)
    producttype = models.ForeignKey(ProductType)
    productproperty = models.ForeignKey(ProductProperty)

    def __str__(self):
        return self.product_text

@python_2_unicode_compatible  # 如果你需要支持Python 2
class Park(models.Model):
    park_text = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    opdate = models.DateTimeField(auto_now=True)
    delflag = models.BooleanField(default=False)

    def __str__(self):
        return self.park_text


@python_2_unicode_compatible  # 如果你需要支持Python 2
class AccessPark(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    def __str__(self):
        return self.park.park_text+" " + self.product.product_text


@python_2_unicode_compatible  # 如果你需要支持Python 2
#代理商类别
class AgentType(models.Model):
    agenttype_text=models.CharField(max_length=20)
    opdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agenttype_text


@python_2_unicode_compatible  # 如果你需要支持Python 2
#代理商
class Agent(models.Model):
    agent_text = models.CharField(max_length=50)
    agenttype = models.ForeignKey(AgentType,on_delete=models.CASCADE)
    opdate = models.DateTimeField(auto_now=True)
    delflag = models.BooleanField(default=False)

    def __str__(self):
        return self.agent_text + "--" + self.agenttype.agenttype_text


@python_2_unicode_compatible  # 如果你需要支持Python 2
#代理商可售产品管理
class AgentProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    opdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent.agent_text + "    " + self.product.product_text + "    " + self.opdate.strftime('%Y-%m-%d %H:%M:%S')


#终端管理
@python_2_unicode_compatible  # 如果你需要支持Python 2
class Terminal(models.Model):
    terminal_text = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    delflag = models.BooleanField(default=False)
    opdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.terminal_text + "   " + self.opdate.strftime('%Y-%m-%d %H:%M:%S')
        #%Y-%m-%d %H:%M:%S


