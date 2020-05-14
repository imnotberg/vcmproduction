#!"C:\Users\adil\Desktop\New folder (2)\customer_portal-master\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'hubspot3==3.2.44','console_scripts','hubspot3'
__requires__ = 'hubspot3==3.2.44'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('hubspot3==3.2.44', 'console_scripts', 'hubspot3')()
    )
