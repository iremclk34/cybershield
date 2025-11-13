import socket
import subprocess
import platform

def ag_taramasi(baslangic, bitis):
    print("\nAğ Taraması Başlatılıyor...\n")
    for i in range(baslangic, bitis + 1):
        ip = f"192.168.1.{i}"
        param = "-n" if platform.system().lower() == "windows" else "-c"
        komut = ["ping", param, "1", ip]
        sonuc = subprocess.call(komut)
        if sonuc == 0:
            print(f"{ip} → CEVAP VERİYOR")
        else:
            print(f"{ip} → ULAŞILAMIYOR")
            ag_taramasi(1,10)  #

print("\nTarama tamamlandı.")