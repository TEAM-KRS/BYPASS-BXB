import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("chmod 777 PROTECT64")
    import PROTECT64

elif bit == '32bit':
    os.system("chmod 777 PROTECT32")
    import PROTECT32
