#!/bin/bash

IPNET="192.168.74.137"
SPORT="30002"

{
    sleep 1
    echo "enable"
    sleep 1
    echo "configure terminal"
    sleep 1
    echo "vlan 10"
    sleep 1
    echo " name VLAN10"
    sleep 1
    echo "exit"
    sleep 1
    echo "vlan 20"
    sleep 1
    echo " name VLAN20"
    sleep 1
    echo "exit"
    sleep 1
    echo "interface FastEthernet0/1"
    sleep 1
    echo " switchport mode access"
    sleep 1
    echo " switchport access vlan 10"
    sleep 1
    echo "exit"
    sleep 1
    echo "interface FastEthernet0/2"
    sleep 1
    echo " switchport mode access"
    sleep 1
    echo " switchport access vlan 20"
    sleep 1
    echo "exit"
    sleep 1
    echo "write memory"
    sleep 1
    echo "disconnect"
    echo "close"
} | telnet $IPNET $SPORT

sleep 2

# Memastikan script keluar dengan kode status yang benar
if [ $? -eq 0 ]; then
    echo "Konfigurasi VLAN dan Interface berhasil diterapkan."
else
    echo "Terjadi kesalahan saat menerapkan konfigurasi."
fi