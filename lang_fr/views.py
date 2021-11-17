from django.shortcuts import render
from django.utils.translation import activate, gettext as _

def french(request):
    # translate in french
    activate('fr')
    transl = _('hello')
    transl2 = _("In this Python Django tutorial I will take you through the basics of setting up internationalization in Django so that you your.")
    transl3 = _("Python Django - Multiple Languages - Internationalization - Part 1")
    return render(request, 'lang_fr/french.html', {
        'transl':transl,
        'transl2':transl2,
        'transl3':transl3,
        })

def elsefrench(request):
    transl = _('hello')
    transl2 = _("In this Python Django tutorial I will take you through the basics of setting up internationalization in Django so that you your.")
    transl3 = _("Python Django - Multiple Languages - Internationalization - Part 1")
    return render(request, 'lang_fr/elsefrench.html', {
        'transl':transl,
        'transl2':transl2,
        'transl3':transl3,
        })