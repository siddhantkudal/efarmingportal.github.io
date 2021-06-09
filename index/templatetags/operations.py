from django import template

register = template.Library()

@register.filter(name='price_order')
def price_order(i,quan):
    result = i.price * int(quan)
    return result