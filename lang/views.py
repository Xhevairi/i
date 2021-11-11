from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

# using getext as _
def home(request):
    trans = _('hello')
    # using translate func
    # trans = translate(language = 'fr')
    return render(request, 'lang/home.html', {'trans': trans})

def item(request):
    return render(request, 'lang/item.html')

# # translate words
# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         text = gettext('hello')
#     finally:
#         activate(cur_language)
#     return text