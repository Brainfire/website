from django import template
from django.template import NodeList
from django.core.urlresolvers import reverse
from django.template import resolve_variable
from django.contrib.auth.models import Group

register = template.Library()

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.simple_tag
def boolpretty(boolToPretty):
    if(boolToPretty):
        return "Yes"
    return "No"

@register.tag()
def ifusergroup(parser, token):
    """ Check to see if the currently logged in user belongs to a specific
    group. Requires the Django authentication contrib app and middleware.

    Usage: {% ifusergroup Admins %} ... {% endifusergroup %}, or
           {% ifusergroup Admins|Group1|Group2 %} ... {% endifusergroup %}, or
           {% ifusergroup Admins %} ... {% else %} ... {% endifusergroup %}

    """
    try:
        tag, group = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Tag 'ifusergroup' requires 1 argument.")
    
    nodelist_true = parser.parse(('else', 'endifusergroup'))
    token = parser.next_token()
    
    if token.contents == 'else':
        nodelist_false = parser.parse(('endifusergroup',))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    
    return GroupCheckNode(group, nodelist_true, nodelist_false)


class GroupCheckNode(template.Node):
    def __init__(self, group, nodelist_true, nodelist_false):
        self.group = group
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false
    def render(self, context):
        user = resolve_variable('user', context)
        
        if not user.is_authenticated():
            return self.nodelist_false.render(context)
            
        try:
            for group in self.group.split("|"):
                
                if Group.objects.get(name=group) in user.groups.all():
                    return self.nodelist_true.render(context)

        except Group.DoesNotExist:
            return self.nodelist_false.render(context)
            
        
        return self.nodelist_false.render(context)