import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename='/var/www/html/hotbot/logs/hotbot.log', format='%(asctime)s %(message)s')
sys.path.insert(0, '/var/www/html/hotbot')
sys.path.insert(0, '/var/www/html/hotbot/venv/lib/python3.9/site-packeges')
# import app as application