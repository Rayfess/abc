import telnetlib

# Variabel
IP = "192.168.74.128"
PORT = 30026
VLAN_ID = "10"       # Ganti dengan VLAN ID yang sesuai

# Membuat koneksi Telnet
tn = telnetlib.Telnet(IP, PORT, 10)

# Masuk ke mode enable
tn.write(b"enable\n")

# Masuk ke mode konfigurasi
tn.write(b"configure terminal\n")

# Konfigurasi interface e0/1
tn.write(b"interface e0/1\n")
tn.write(b"no shutdown\n")
tn.write(b"switchport mode access\n")
tn.write(f"switchport access vlan {VLAN_ID}\n".encode('ascii'))
tn.write(b"exit\n")

# Konfigurasi interface e0/0
tn.write(b"interface e0/0\n")
tn.write(b"no shutdown\n")
tn.write(b"switchport trunk encapsulation dot1q\n")
tn.write(b"switchport mode trunk\n")
tn.write(b"exit\n")

# Keluar dari mode konfigurasi
tn.write(b"end\n")
tn.write(b"write memory\n")
tn.write(b"exit\n")

# Menutup koneksi
tn.close()