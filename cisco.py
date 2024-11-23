import paramiko

# Setup koneksi SSH
hostname = '192.168.17.1'  # Ganti dengan IP Cisco IOL switch Anda
port = 22  # Port SSH default
username = 'admin'  # Username yang telah Anda buat di perangkat
password = 'cisco'  # Password yang telah Anda buat di perangkat

# Membuat SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def send_command(ssh_shell, command):
    """Mengirim perintah ke shell SSH dan mengembalikan output."""
    ssh_shell.send(command + '\n')
    # Tunggu hingga ada data yang tersedia untuk dibaca
    while not ssh_shell.recv_ready():
        pass
    output = ssh_shell.recv(5000).decode('utf-8')
    return output

try:
    # Connect ke perangkat
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port=port, username=username, password=password)

    # Mengambil channel SSH
    ssh_shell = client.invoke_shell()

    # Mulai konfigurasi
    print(send_command(ssh_shell, 'conf t'))  # Masuk ke mode konfigurasi
    print(send_command(ssh_shell, 'hostname CiscoSW'))  # Mengubah hostname
    print(send_command(ssh_shell, 'interface vlan 1'))  # Masuk ke interface VLAN 1
    print(send_command(ssh_shell, 'ip address 192.168.17.1 255.255.255.0'))  # Menetapkan IP address pada VLAN 1
    print(send_command(ssh_shell, 'no shutdown'))  # Mengaktifkan interface VLAN 1
    print(send_command(ssh_shell, 'exit'))  # Keluar dari konfigurasi interface
    print(send_command(ssh_shell, 'exit'))  # Keluar dari mode konfigurasi

    # Menjalankan perintah untuk melihat konfigurasi yang telah diterapkan
    output = send_command(ssh_shell, 'show running-config')
    print(output)

except paramiko.SSHException as e:
    print(f"SSH connection error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Menutup koneksi SSH
    print("Closing the connection...")
    client.close()