from django import template

register = template.Library()



@register.filter
def isnone(value):
    ''' strict value = None test '''
    if value == None:
        return True
    else:
        return False


@register.filter
def isempty(value):
    ''' none or empty = True test '''

    if isnone(value):
        return True

    try:
        length = len(value)
        if length == 0:
            return True
        else:
            return False
    except:
        return False


@register.filter
def isset(value):
    ''' none or empty = False test '''
    return not isempty(value)
