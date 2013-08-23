import markdown2

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    extensions = ["nl2br", ]

    return mark_safe(markdown2.markdown(force_unicode(value),
                                        safe_mode=True,
                                        extras=["code-friendly",
                                                "fenced-code-blocks",
                                        ]))

