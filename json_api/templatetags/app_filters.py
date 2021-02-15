from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter
def in_category(time, user):
    return time.filter(user_id=user)