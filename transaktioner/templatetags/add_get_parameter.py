from django.template import Library, Node, Variable

register = Library()

class AddGetParameter(Node):
    def __init__(self, values):
        self.values = values

    def render(self, context):
        req = Variable('request').resolve(context)
        params = req.GET.copy()
        for key, values in self.values.items():
            params[key] = values.resolve(context)
        if params.urlencode() != '':
            return '?%s' % params.urlencode()
        else:
            return ''

@register.tag
def add_get(parser, token):
    pairs = token.split_contents()[1:]
    values = {}
    for pair in pairs:
        s = pair.split('=', 1)
        values[s[0]] = parser.compile_filter(s[1])
    return AddGetParameter(values)
