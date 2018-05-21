# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product,Park,AccessPark,Agent,AgentType,AgentProduct,Terminal,ProductType,ProductProperty
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_text', 'code','price','saleflag','comment','opdate')

class ParkAdmin(admin.ModelAdmin):
    list_display = ('park_text','comment','opdate')

class AgentTypeAdmin(admin.ModelAdmin):
    list_display = ('agenttype_text','opdate')

class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_text','opdate')

class TerminalAdmin(admin.ModelAdmin):
    list_display =('terminal_text','comment','opdate')

class MyAdminSite(admin.AdminSite):
    site_header = '欢畅智慧旅游后台管理系统 V1.0'
    site_title ="欢畅管理系统"

# Register your models here.
admin_site = MyAdminSite()
admin_site.register(Product,ProductAdmin)

# admin.site.register(Product,ProductAdmin)
admin_site.register(Park,ParkAdmin)
admin_site.register(AccessPark)
admin_site.register(AgentType,AgentTypeAdmin)
admin_site.register(Agent)
admin_site.register(AgentProduct)
admin_site.register(Terminal,TerminalAdmin)
admin_site.register(ProductProperty)
admin_site.register(ProductType)
