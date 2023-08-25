from django import template

register = template.Library()


@register.simple_tag
def percentage(*args, **kwargs):
    print(kwargs, args)
    count_in_city = kwargs["count_in_city"]
    all_count = kwargs["all_count"]
    return count_in_city / all_count