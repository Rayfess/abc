from netmiko import ConnectHandler

# Informasi perangkat Cisco IOL menggunakan Telnet
device = {
    'device_type': 'cisco_ios_telnet',  # Menandakan menggunakan Telnet
    'host': '192.168.74.128',              # IP perangkat Cisco IOL Anda
    'username': 'admin',                # Username untuk login
    'password': 'password',             # Password untuk login
    'secret': 'enable_password',        # Password untuk enable mode
    'port': 30026,                         # Port Telnet, default adalah 23
}

# Membuat koneksi menggunakan Netmiko
try:
    with ConnectHandler(**device) as net_connect:
        # Masuk ke enable mode
        net_connect.enable()

        # Menyiapkan konfigurasi interface
        config_commands = [
            'en'
            'conf t'
            'int e0/0',   # Pilih interface yang akan dikonfigurasi
            'description "Connected to Server"',
            'no shutdown',                      # Mengaktifkan interface
            'ip address 192.168.17.1 255.255.255.0'  # Mengonfigurasi IP address
        ]
        
        # Mengirimkan perintah konfigurasi ke perangkat
        output = net_connect.send_config_set(config_commands)

        # Menampilkan output konfigurasi
        print(output)

        # Menyimpan konfigurasi ke startup-config
        net_connect.save_config()

except Exception as e:
    print(f"Terjadi kesalahan saat mencoba menghubungkan ke perangkat: {e}")
