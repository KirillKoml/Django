from django import template


register = template.Library()


@register.simple_tag()
def media(path):
    if path:
        return f"media/{path}"
    return "#"