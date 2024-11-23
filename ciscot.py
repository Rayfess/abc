import telnetlib
import time

# Variabel untuk IP dan port switch
IP = "192.168.74.128"  # Ganti dengan alamat IP switch Anda
PORT = 30026          # Port default untuk Telnet

# Fungsi untuk menghubungkan ke switch
def connect_to_switch(ip, port):
    # Membuat koneksi Telnet
    tn = telnetlib.Telnet(ip, port)
    return tn

# Fungsi untuk mengirimkan perintah ke switch
def send_command(tn, command):
    tn.write(command.encode('ascii') + b"\n")
    time.sleep(1)  # Tunggu sebentar untuk memastikan perintah diproses

# Fungsi untuk mengkonfigurasi switch
def configure_switch(tn):
    send_command(tn, b"enable")
    send_command(tn, b"configure terminal")

    # Konfigurasi interface e0/1
    send_command(tn, b"interface e0/1")
    send_command(tn, b"no shutdown")  # Mengaktifkan interface
    send_command(tn, b"switchport mode access")  # Mengatur mode akses
    send_command(tn, b"switchport access vlan 10")  # Mengatur VLAN
    send_command(tn, b"exit")  # Kembali ke mode konfigurasi

    # Konfigurasi interface e0/0
    send_command(tn, b"interface e0/0")
    send_command(tn, b"no shutdown")  # Mengaktifkan interface
    send_command(tn, b"switchport trunk encapsulation dot1q")  # Mengatur encapsulation trunk
    send_command(tn, b"switchport mode trunk")  # Mengatur mode trunk
    send_command(tn, b"exit")  # Kembali ke mode konfigurasi

    # Keluar dari mode konfigurasi
    send_command(tn, b"end")
    send_command(tn, b"write memory")  # Menyimpan konfigurasi
    send_command(tn, b"exit")  # Keluar dari sesi

# Main script
if __name__ == "__main__":
    # Menghubungkan ke switch
    tn = connect_to_switch(IP, PORT)
    
    # Mengkonfigurasi switch
    configure_switch(tn)

    # Menutup koneksi
    tn.close()
    print("Konfigurasi switch selesai.")