from .base import *

# try:
# 	from .local import *
# 	live = False
# except:
# 	live = True
live = False

if live:
	from .production import *
