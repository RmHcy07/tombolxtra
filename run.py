import os,sys,time
from time import sleep

os.system('clear')
print('\t\033[00mTombol termux\n\t\033[90m_____________\033[00m')
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
ainx = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
ainx.write(key)
ainx.close()
sleep (2)
os.system('termux-reload-settings')
print ("\033[00m[\033[96m*\033[00m]Done.")
sleep (2)
sys.exit()
