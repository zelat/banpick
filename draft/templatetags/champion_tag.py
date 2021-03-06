from django import template
from django.utils import timezone
from draft.models import Draft
import re, os, datetime

register = template.Library()


@register.filter
def sp_position(no):
    return -int(no)*82

@register.simple_tag
def player_name(name, no):
    name_list = name.split('//')
    lane_list = ['[上单]', '[打野]', '[中单]', '[下路]', '[辅助]']
    no = int(no)
    return lane_list[no] + name_list[no] if name_list[no] else lane_list[no]
