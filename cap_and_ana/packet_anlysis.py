#!/usr/bin/env python
# coding: shift-jis

from scapy.all import *
from datetime import datetime
import tkinter
from tkinter import filedialog
import os.path


idir = './cap_result'
file_path = tkinter.filedialog.askopenfilename(initialdir = idir)
print(f"basename: {os.path.basename(file_path)}")
file_name = os.path.basename(file_path)

PCAP_filename = file_path

def parse_pcap(filename):

    packets = rdpcap(filename)
    packets.summary()

    print("----------------------------------")
    for cnt, packet in enumerate(packets, 1):
        datetime_text = datetime.fromtimestamp(packet.time).isoformat()
        print("No:", cnt, " ", datetime_text, " ", packet.summary())
    print("----------------------------------")

if __name__ == "__main__":

    parse_pcap(PCAP_filename)

    print("completed.")