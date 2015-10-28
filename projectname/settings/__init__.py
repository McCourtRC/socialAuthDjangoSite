#Settings for multiple environments
from .base import *

#local settings
try:
    from .local import *
except:
    pass

#production settings
try:
    from .production import *
except:
    pass
