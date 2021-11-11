from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
# from .models import trans_texts, translate

# using getext as _
def home(request):
    trans = _('hello')
    # using translate() func
    # trans = translate(language = 'fr')
    return render(request, 'lang/home.html', {'trans': trans})

def item(request):
    return render(request, 'lang/item.html')

# # texts in default language
# def trans_texts():
#     texts = (
#             'Hello, '
#             'hello',
#             'Language',
#             'home',
#             'item',
#             'In this Python Django tutorial I will take you through the basics of setting up internationalization in Django so that you your.',
#             'Python Django - Multiple Languages - Internationalization - Part 1'
#         )
#     return texts 

# # translate texts
# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         texts = trans_texts()
#         for text in texts:
#             text = gettext(text)
#     finally:
#         activate(cur_language)
#     return text