import paramiko
import time

# Setup koneksi SSH
hostname = '192.168.17.1'  # Ganti dengan IP Cisco IOL switch Anda
port = 22  # Port SSH default
username = 'admin'  # Username yang telah Anda buat di perangkat
password = 'cisco'  # Password yang telah Anda buat di perangkat

# Membuat SSH client
client = paramiko.SSHClient()

# Menambahkan host ke known hosts (jika belum ada)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect ke perangkat
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port=port, username=username, password=password)

    #Mengambil channel SSH
    ssh_shell = client.invoke_shell()

    time.sleep(1)

    #mulai konfigurasi
    ssh_shell.send('conf t\n')  # Masuk ke mode konfigurasi
    time.sleep(1)
    ssh_shell.send('hostname CiscoSW\n')  # Mengubah hostname
    time.sleep(1)
    ssh_shell.send('interface vlan 1\n')  # Masuk ke interface VLAN 1
    time.sleep(1)
    ssh_shell.send('ip address 192.168.17.1 255.255.255.0\n')  # Menetapkan IP address pada VLAN 1
    time.sleep(1)
    ssh_shell.send('no shutdown\n')  # Mengaktifkan interface VLAN 1
    time.sleep(1)
    ssh_shell.send('exit\n')  # Keluar dari konfigurasi interface
    time.sleep(1)
    ssh_shell.send('exit\n')  # Keluar dari mode konfigurasi
    time.sleep(1)

    # Menjalankan perintah untuk melihat konfigurasi yang telah diterapkan
    ssh_shell.send('show running-config\n')
    time.sleep(2)
    output = ssh_shell.recv(5000).decode('utf-8')  # Menangkap output dari perintah
    print(output)

finally:
    # Menutup koneksi SSH
    print("Closing the connection...")
    client.close()
