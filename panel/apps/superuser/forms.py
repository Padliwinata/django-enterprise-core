'''
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# File: forms.py
# Project: django-panel-core
# File Created: Wednesday, 22nd August 2018 12:50:12 am
# 
# Author: Arif Dzikrullah
#         ardzix@hotmail.com>
#         https://github.com/ardzix/>
# 
# Last Modified: Wednesday, 22nd August 2018 12:50:13 am
# Modified By: arifdzikrullah (ardzix@hotmail.com>)
# 
# Hand-crafted & Made with Love
# Copyright - 2018 Ardz Co, https://github.com/ardzix/django-panel-core
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

from django.forms import *
from .models import *
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = {
            'name' :  models.CharField(max_length=255),
            'permissions' : ModelMultipleChoiceField(
                    queryset = Permission.objects.all(),
                )
        }

class PermissionForm(ModelForm):
    class Meta:
        model = Permission
        fields = {
            'name' :  models.CharField(max_length=255),
            'codename' :  models.CharField(max_length=255),
            'content_type' : ModelChoiceField(
                    queryset = ContentType.objects.all(),
                )
        }