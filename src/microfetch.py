#!/usr/bin/env/python
# | microfetch 0.2
# | written by VeryEpicKebap - June 23rd 2025

import os
import argparse
from mfetch_config import *
global used
RESET = "\033[0m"
COLORS = {
    "Arch":     "\033[38;5;39m",     
    "Debian":   "\033[38;5;160m",   
    "Ubuntu":   "\033[38;5;208m",   
    "Fedora":   "\033[38;5;27m",   
    "Manjaro":  "\033[38;5;35m",   
    "Gentoo":   "\033[38;5;105m", 
    "Void":     "\033[38;5;34m",   
    "Android":  "\033[38;5;46m",   
    "FreeBSD":  "\033[38;5;160m", # revision 2: bsd support added  
    "OpenBSD":  "\033[38;5;226m",
    "NetBSD":   "\033[38;5;208m",  
    "DragonFly": "\033[38;5;161m", 
}
def get_distro():
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME="):
                    return line.split("=", 1)[1].strip().strip('"')
    except FileNotFoundError:
        pass
    if os.path.exists("/system/build.prop"):
        return "Android (detected)"
    try:
        with open("/proc/version") as f:
            version = f.read().lower()
            if "android" in version:
                return "Android"
    except FileNotFoundError:
        pass
    sysname = os.uname().sysname.lower()
    if "bsd" in sysname:
        return os.uname().sysname
    return "Unknown"
def dc(distro_name):
    for key in COLORS:
        if key.lower() in distro_name.lower():
            return COLORS[key] + distro_name + RESET
    return distro_name
dname=dc(get_distro())
with open("/sys/devices/virtual/dmi/id/product_name") as f:
    model=f.read().strip()
cpui=os.popen("grep -m1 -i 'model name' /proc/cpuinfo").read().strip().split(":", 1)[1]
addons={
     "001": f"System: {get_distro()}",
     "002": f"System: {dname}",
     "003": f"Kernel: {os.uname().release}",
     "004": f"Version: {os.uname().version}",
     "005": f"Host: {os.uname().version}",
     "006": f"CPU:{cpui}",
     "007": f"Model: {model}",
}
dnc = addons.get("001")
dcl = addons.get("002")
rel = addons.get("003")
ver = addons.get("004")
cpu = addons.get("006")
mod = addons.get("007")    
user=os.getlogin()

def main():
    global dname
    uname = os.uname()
    print(f"\n------ {user} ------");outp='\n'.join(used);print(outp, "\n-------------------\n")

if __name__ == "__main__":
    main()
