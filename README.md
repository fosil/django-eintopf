# django-eintopf
Collection of small tools and enhancements for Django

## Templatetags

### "Core"
**use:** ``{% load eintopf %}``

#### Filters

##### isnone ``{{ value|isnone }}``
Strict test if 'value' is None. Return True or False.

##### isempty ``{{ value|isempty }}``
If 'value' is None or empty string/number or list/dict without items return True.

##### isset ``{{ value|isempty }}``
If 'value' is not None or non-empty string/number or list/dict have items return True.
