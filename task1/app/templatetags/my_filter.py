from django import template

register = template.Library()

@register.filter
def value_to_color(value):
    if float(value) < 0 :
        return('147C30')
    elif float(value) <= 1:
        return('FFFFFF')
    elif 1 < float(value) <= 2:
        return('FF9999')
    elif 2 < float(value) <= 5:
        return('FF6666')
    elif float(value) > 5:
        return('FF3333')
    return(value)