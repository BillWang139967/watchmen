# coding:utf8

import sys
import os
import django

from Monitor import settings
from monitor.backends import data_processing

django.setup()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Monitor.settings")

if __name__ == '__main__':
    reactor = data_processing.DataHandler(settings)
    reactor.loopping()
