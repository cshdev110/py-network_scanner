#!/usr/bin/env python

# The script needs to be executed as superuser.
import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


scan("192.168.180.0/24")
