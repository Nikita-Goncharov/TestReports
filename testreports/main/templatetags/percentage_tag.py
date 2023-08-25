from django import template

register = template.Library()


@register.simple_tag
def percentage(*args, **kwargs):
    count_in_city = kwargs["count_in_city"]
    all_count = kwargs["all_count"]
    return count_in_city / all_count * 100