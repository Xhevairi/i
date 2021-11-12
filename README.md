<!-- translation in Django -->
Demo - Translation in Django
============================

Translate in french
-------------------  
A simple translation example  
    - Case one, only french - in _lang_fr/views.py_: import _activate()_ and _gettext()_  
    - Case two - in template: load _i18n_, use _language tag_ to activate franch language, and use _translate tag_  

Install gettext
----------------
Installation is depending on operating system: it is different for Mac, Linux, Windows, etc.  
See Django Documentation for Internacionalization  
Clone this project then run:  
    - py manage.py makemessages --all  
    - py manage.py compilemessages  