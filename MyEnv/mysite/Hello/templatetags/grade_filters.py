from django import template
register = template.Library()

@register.simple_tag
def add(a, values):
    for i in values:
        if i.stonks>0:
            a+=i.stonks
    return a
@register.simple_tag
def add_s(a, values):
    for i in values:
        if i.stonks<=0:
            a+=i.stonks
    return a

@register.simple_tag
def ADD(a, values):
    for v in values:
        for i in v:
            if i.stonks>0:
                a+=int(i.stonks)
    return a

@register.simple_tag
def ADD_S(a, values):
    for v in values:
        for i in v:
            if i.stonks<=0:
                #print(i.stonks)
                a+=int(i.stonks)
    return a
@register.simple_tag
def Budget(a, values):
    for v in values:
        for i in v:
            a+=int(i.stonks)
    return a
@register.simple_tag
def budget(a, values):
    for i in values:
        a+=i.stonks
    return a