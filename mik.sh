#!/bin/bash

IPNET="192.168.74.137"
MIKROTIK_IP="192.168.200.1"     # IP MikroTik yang baru
MIKROTIK_S="192.168.200.0"
MIKROTIK_R="192.168.200.2-192.168.200.200"
USER_MIKROTIK="admin"           # Username SSH default MikroTik
PASSWORD_MIKROTIK=""            # Kosongkan jika MikroTik tidak memiliki password
MPORT="30004"
VLAN_ID=10
$IP_Pref="/24"
IP_Router="192.168.$IP_A.1"
IP_Subnet="192.168.$IP_A.0"
$IP_A="17"

{
    echo "admin"
    sleep 1
    echo ""
    sleep 1
    echo "n"
    sleep 1
    echo "123"
    sleep 1
    echo "123"
    sleep 1
    echo "/interface vlan add name=vlan10 vlan-id=$VLAN_ID interface=ether1"
    sleep 1
    echo "/ip address add address=$IP_Router$IP_Pref interface=vlan10"
    sleep 1
    echo "/ip address add address=$MIKROTIK_IP$IP_Pref interface=ether2"
    sleep 1
    echo "/ip pool add name=dhcp_pool ranges=$MIKROTIK_R"
    sleep 1
    echo "/ip dhcp-server add name=dhcp1 interface=ether2 address-pool=dhcp_pool"
    sleep 1
    echo "/ip dhcp-server network add address=$MIKROTIK_S$IP_Pref gateway=$MIKROTIK_IP"
    sleep 1
    echo "/ip dhcp-server enable dhcp1"
    sleep 1
    echo "/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade"
    sleep 1
    echo "/ip route add dst-address=$IP_Subnet$IP_Pref gateway=$IP_Router"
    sleep 1
    
} | telnet $IPNET $MPORT

sleep 2




#  Konfigurasi MikroTik melalui SSH tanpa prompt
# echo "Mengonfigurasi MikroTik..."
# if [ -z "$PASSWORD_MIKROTIK" ]; then
#     ssh -o StrictHostKeyChecking=no $USER_MIKROTIK@$MIKROTIK_IP <<EOF
# interface vlan add name=vlan10 vlan-id=$VLAN_ID interface=ether1
# ip address add address=$IP_Router$IP_Pref interface=vlan10      # Sesuaikan dengan IP di VLAN Ubuntu
# ip address add address=$MIKROTIK_IP$IP_Pref interface=ether2     # IP address MikroTik di network lain
# ip route add dst-address=$IP_Router$IP_Pref gateway=$IP_Router
# EOF
# else
#     sshpass -p "$PASSWORD_MIKROTIK" ssh -o StrictHostKeyChecking=no $USER_MIKROTIK@$MIKROTIK_IP <<EOF
# interface vlan add name=vlan10 vlan-id=$VLAN_ID interface=ether1
# ip address add address=$IP_Router$IP_Pref interface=vlan10      # Sesuaikan dengan IP di VLAN Ubuntu
# ip address add address=$MIKROTIK_IP$IP_Pref interface=ether2     # IP address MikroTik di network lain
# ip route add dst-address=$IP_Router$IP_Pref gateway=$IP_Router
# EOF
# fi