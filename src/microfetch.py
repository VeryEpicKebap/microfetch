#!/usr/bin/python3
# | microfetch 0.4
# | written by VeryEpicKebap - June 23rd 2025

v="microfetch (version 0.4)"
import os
import argparse
import subprocess
import sys
sys.path.insert(0,f"{os.getcwd}")
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
        return "Android"
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
# revision 4: ascii art logos
# logo-related parts of this program were hardcoded for use in Arch Linux only. future updates will bring logo support for every distro detectable by this program.,
arch = [
  r"      _    ",
  r"     / \   ",
  r"    /   \  ",
  r"   /  .  \ ",
  r"  /._| |_.\ ",
]


user=os.getlogin()
# revision 3: simplified add-on system
class Md:
 usr = f"  ------ {user} ------"
 end = f"  --------------------\n"
 dnc = f"  System: {get_distro()}"
 dcl = f"  System: {dname}"
 rel = f"  Kernel: {os.uname().release}"
 ver = f"  Version: {os.uname().version}"
 hos = f"  Host: {os.uname().nodename}"
 cpu = f"  CPU:{cpui}"
 mod = f"  Model: {model}"
   

def main():
    global dname
    uname = os.uname()
    width = max(len(line) for line in arch)
    for i in range(max(len(arch), len(used))): 
     a = arch[i] if i < len(arch) else ''
     b = used[i] if i < len(used) else ''
     print(f"\033[38;5;39m{a.ljust(width)}{RESET}",b)

if __name__ == "__main__":
    if "-ch" in sys.argv:
     print(f"{v}\navailable display modules")
     for name in vars(Md):
      if not name.startswith("__"):
       print(f"- {name}")
    elif "-v" in sys.argv:
     print(v)
    else:
     main()
