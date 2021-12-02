import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Extra Termux ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  Bye:   MR DANI')
print('\t web : No system is svae')
print('\t Facebook : fb.me/rama.gemers.14')
print('\t Github : https://github.com/RmHcy07')
print('\t TOOLS BY : MAR_HACKED)
print(a+'+'*40)
print('\nLoanjing.....')
sleep()
print(b+'\n[☆] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[☆] Berhasil Ngap !')
sleep(1)
print(b+'\n[☆] menambahkan File Kontrol ..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[☆] Memproses Bentar Asw  !')
sleep(1)
print(b+'\n[☆] Tunggu Sebentar Anjing')
sleep(2)
os.system('termux-reload-settings')
print(a+'[☆] Finish Prosesing !! ^^'+c+'\n\nhubungi : saya lewat Wa No 085842920585*\n\n')
