#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# os.popen("ip addr show dev eth0 | awk '/^ +inet /{ print $2; }'").read().strip()
# above text will extract the device's IP address from the system if the system is linux.

import sys
import socket
import os

from pylcdsysinfo import BackgroundColours, TextColours, TextAlignment, TextLines, LCDSysInfo
from time import sleep

hostname=socket.gethostname()

#Get IP address and concatenate with "IP: " string
ipaddress=socket.gethostbyname(hostname)
ipstring="IP: " + ipaddress
print(ipstring)

if sys.platform == 'darwin':
    ipaddress=socket.gethostbyname(hostname)
    print("Mac detected")
    

d = LCDSysInfo()
d.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
d.dim_when_idle(False)
d.set_brightness(255)
d.save_brightness(127, 255)
d.set_text_background_colour(BackgroundColours.BLACK)

#d.display_cpu_info(8010, 32, TextColours.RED, TextColours.WHITE)
#d.display_ram_gpu_info(1994, 32, TextColours.RED, TextColours.GREEN)
#d.display_network_info(1, 2, TextColours.RED, TextColours.GREEN, 0, 1) 
#d.display_fan_info(1994, 1994, TextColours.RED, TextColours.GREEN)

d.display_text_on_line(2, "Hostname: ", True, TextAlignment.LEFT, TextColours.GREEN)
d.display_text_on_line(3, hostname, True, TextAlignment.LEFT, TextColours.GREEN)
d.display_text_on_line(4, ipstring, True, TextAlignment.LEFT, TextColours.WHITE)
#d.display_text_on_line(5, ipaddress, True, TextAlignment.LEFT, TextColours.WHITE)

sys.exit(0)

