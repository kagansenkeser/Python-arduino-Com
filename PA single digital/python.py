#kodu ben yazmadım internetten aldim
import serial  #haberleşme için kütüphane çektik
import time    # zaman lazim oluyor onun kütüphanesi

arduino = serial.Serial('COM3', baudrate=9600, timeout=1)
#arduino değerini bu arduino da serial dan aldığımız serialdata olan değer olcak onu atıyoruz
#com 3 deme sebebimiz arduino kanalı hız 9600 time out ne bilmiyorum

while (1):
    #sonsuz döngü
    dataFromUser = input("-> ")
    #kullanıcan değer alıyoruz alırken de  -> yazdırıyoruz
    if (dataFromUser == "0"):
        arduino.write(b'0')
    #aldigmiz değer 0 sa arduino daki değere '0' yazdiriyor b koyma sebebimizi bilmiyorum ama koymayınca hata veiryor bazı yerlerde koymuyor

        print("LED turned OFF")
        time.sleep(0.5)  # Sleep 0.5s
        #0.5 saniye bekliyor ki ard arda bi sürü işlem yapmalayım ama görüntü işlemede bu asla olmamalı olursa
        #fps direk 1 e deüşüyor önemli
    if (dataFromUser == "1"):
        arduino.write(b'1')
        print("LED turned ON")
        time.sleep(0.5)  # Sleep 0.5s
