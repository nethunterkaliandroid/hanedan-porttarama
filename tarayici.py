import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Hanedan PORT TARAYICI")
print(ascii_banner)

#hedefi tanımlayalım
if len(sys.argv) == 2:

 #host adresini IPV4 e çevirelim
    target = socket.gethostbyname(sys.argv[1])
else:
  print("Geçersiz miktar")

# Birkan tekkan lamer bannerı
print("-" * 50)
print("Hedef taranıyor: " + target)
print("Tarama başladı:" + str(datetime.now()))
print("-" * 50)

try:

  # will scan ports between 1 to 65,535
  for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    # hata dönütü
    result = s.connect_ex((target,port))
    if result ==0:
       print("{} portu açîk".format(port))
    s.close()

except KeyboardInterrupt:
        print("\n Çıkış yapılıyor !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Host adresi alınamadı !!!!")
        sys.exit()
except socket.error:
        print("\ Sunucu yanıt vermiyor !!!!")
        sys.exit()

#@nethunterROM
#Tüm hakları m12345'e aittir.
