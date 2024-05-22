import os
import sys
import platform

# путь к проекту
sys.path.insert(0, '/home/c/ch88479/django_6h8h6/public_html')
# путь к фреймворку
sys.path.insert(0, '/home/c/ch88479/django_6h8h6/public_html/yandex2mqtt')
# путь к виртуальному окружению
python_version = ".".join(platform.python_version_tuple()[:2])
sys.path.insert(0, '/home/c/ch88479/django_6h8h6//django/lib/python{0}/site-packages'.format(python_version))
os.environ["DJANGO_SETTINGS_MODULE"] = "yandex2mqtt.settings"


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from apps.main.utils import run_background_mqtt_listeners

run_background_mqtt_listeners()
