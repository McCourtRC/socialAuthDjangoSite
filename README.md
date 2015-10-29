# Django website - basic
DEVELOPMENT INSTALLATIONS:
- Virtualenv                  '[sudo] easy_install virtualenv' ,
                              (cd to dir for virtual env and 'virtualenv .')

SERVER INSTALLATIONS:
- Python 2.7
- Django 1.8.3                'pip install Django==1.8.3'
- Django AllAuth              'pip install django-allauth'
                              reference http://django-allauth.readthedocs.org/en/latest/installation.html
- Crispy_forms                'pip install --upgrade django-crispy-forms'



PROJECT INSTALLATIONS:
- Bootstrap                   (either use cdn or directly copy missing files into static)
- Registration redux helpers  https://github.com/codingforentrepreneurs/Try-Django-1.8/tree/master/src/templates ,
                              copy the registration folder into templates

TODO BEFORE PRODUCTION:
- Debug                       set DEBUG to False in settings ,
                              remove static settings set for settings.DEBUG,
                              update ALLOWED_HOSTS
- Email                       set valid email in settings (may require unlock captcha),
                              update activation_email.txt
- Auth                        set consumer secret and key values for third party authentication
- STATIC/MEDIA                set up static and media servers in settings
- PostgreSQL                  set up database in settings
- Sites                       update sites in admin page
- Custom auth                 https://codingforentrepreneurs.com/projects/simple-custom-auth/,
                              https://codingforentrepreneurs.com/projects/django-allauth/,
                              references to create custom authentication
- Backend                     Django query sets for views.py
- Cleanup                     remove unnecessary debug code from head.html

PRODUCTION
-                             delete local.py !!!
-                             set production settings
-                             create error pages 400, 403, 404, 500.html
-                             update ADMINS in settings for 500 alerts
