#!C:\Users\HALAL\PACMANN.ai\Wrangling\pipeline\pras_wrangling\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'fonttools','console_scripts','pyftsubset'
__requires__ = 'fonttools'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('fonttools', 'console_scripts', 'pyftsubset')()
    )
