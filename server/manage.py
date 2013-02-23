#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

    from django.core.management import execute_from_command_line
    
    ROOT_PATH = os.path.dirname(__file__)
    if ROOT_PATH not in sys.path:
    	sys.path.append(ROOT_PATH)

    execute_from_command_line(sys.argv)
