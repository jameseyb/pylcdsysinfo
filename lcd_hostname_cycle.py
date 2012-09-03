#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import socket
import time

from pylcdsysinfo import BackgroundColours, TextColours, TextAlignment, TextLines, LCDSysInfo
from time import sleep

hostname=socket.gethostname()

#Get IP address and concatenate with "IP: " string
t_ipaddress=socket.gethostbyname(hostname)
ipaddress="IP: " + t_ipaddress
    
d = LCDSysInfo()
d.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
d.dim_when_idle(False)
d.set_brightness(255)
d.save_brightness(127, 255)
d.set_text_background_colour(BackgroundColours.BLACK)

while True:
    d.display_text_on_line(2, "Hostname: ", True, TextAlignment.LEFT, TextColours.GREEN)
    d.display_text_on_line(4, ipaddress, True, TextAlignment.LEFT, TextColours.WHITE)
    time.sleep(5)
    d.display_text_on_line(2, hostname, True, TextAlignment.LEFT, TextColours.GREEN)
    d.display_text_on_line(4, ipaddress, True, TextAlignment.LEFT, TextColours.WHITE)
    time.sleep(5)
    d.clear_lines(TextLines.ALL, BackgroundColours.BLACK)

sys.exit(0)

