import os
os.system("""
apt update && apt upgrde
pkg update
pkg upgrade
pkg install git
pkg install curl
pkg install wget
pkg install nano
pkg install proot
pkg install termux-api
pkg install unzip
pkg install tar
pkg insall python
pkg install python2
pkg install pip
pkg install pip2
pip install mediafire_dl
pip install git+https://github.com/Juvenal-Yescas/mediafire-dl
clear
""")
import mediafire_dl

url = 'https://www.mediafire.com/file/oywuzlzwlsmnizc/password-rv.zip/file'
output = 'RvToo.zip'
mediafire_dl.download(url, output, quiet=False)
os.system("clear")
print ("""
rv ﺩﺭﻮﺳﺎﺑ
rv ﺭﻭﺮﻣ ﻪﻤﻠﻛ
password rv
rv ﺮﺴﻟﺍ ﻪﻤﻠﻛ
😁ﺢﻴﺿﻮﺗ ﻪﻳﺎﻔﻛ


""")
os.system ("""
unzip RvToo.zip
cd RvTool
bash install.sh

""")
