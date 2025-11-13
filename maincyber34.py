import platform
import socket
import os
import datetime

def sistem_bilgilerini_goster():
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("🔍 - Sistem Bilgileri -\n")
        f.write(f"İşletim Sistemi: {platform.system()}\n")
        f.write(f"Sürüm: {platform.version()}\n")
        f.write(f"Makine: {platform.machine()}\n")
        f.write(f"İşlemci: {platform.processor()}\n")
        f.write(f"Bilgisayar Adı: {socket.gethostname()}\n")
        f.write(f"IP Adresi: {socket.gethostbyname(socket.gethostname())}\n")
        f.write(f"Kullanıcı Adı: {os.getlogin()}\n")
        f.write(f"Giriş Zamanı: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

sistem_bilgilerini_goster()
