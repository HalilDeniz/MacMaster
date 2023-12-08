import os
import re
import random
import requests
import argparse
import netifaces
import subprocess
from scapy.all import sniff
from scapy.layers.inet import IP
from colorama import Fore, Style, init

from utils.version import __version__



init()  # Colorama'yı başlat


def packet_callback(packet):
   try:
       source_mac      = packet.src
       destination_mac = packet.dst
       source_ip       = packet[IP].src if IP in packet else "No IP"
       destination_ip = packet[IP].dst if IP in packet else "No IP"
       print(f"{Fore.GREEN}Source Mac     :{Style.RESET_ALL} {source_mac} ==> {Fore.GREEN}Source IP:{Style.RESET_ALL} {source_ip}")
       print(f"{Fore.GREEN}Destination Mac:{Style.RESET_ALL} {destination_mac} ==> {Fore.GREEN}Source IP:{Style.RESET_ALL} {destination_ip}")
   except:
       pass
def start_traffic_monitoring(interface):
    print(f"{Fore.BLUE}Monitoring network traffic on{Style.RESET_ALL} {Fore.GREEN}{interface}...{Style.RESET_ALL}")
    sniff(iface=interface, prn=packet_callback, store=False)

def show_version():
    print(f"MacMaster Version: {__version__}")

def list_network_interfaces():
    interfaces = netifaces.interfaces()
    index = 0
    print("Availables:")
    for interface in interfaces:
        index += 1
        print(f"\t{Fore.CYAN}{index}){Style.RESET_ALL} {interface}")


def save_original_mac(interface):
    mac_address_file = f"/opt/{interface}_original_mac.txt"
    if not os.path.exists(mac_address_file):
        original_mac = get_mac(interface)
        with open(mac_address_file, "w") as file:
            file.write(original_mac)
    return


def get_original_mac(interface):
    mac_address_file = f"/opt/{interface}_original_mac.txt"
    if os.path.exists(mac_address_file):
        with open(mac_address_file, "r") as file:
            original_mac = file.readline().strip()
        return original_mac
    else:
        return None


def get_mac(interface):
    output = subprocess.check_output(["ifconfig", interface], text=True)
    mac = re.search(r'([0-9a-fA-F]{1,2}:){5}[0-9a-fA-F]{1,2}', output)
    if mac:
        return mac.group(0)
    else:
        return None


def generate_random_mac():
    random_mac = [random.randint(0x00, 0xff) for _ in range(6)]
    random_mac[0] &= 0xfe  # Make sure the MAC address is unicast
    random_mac[0] |= 0x02  # Make sure the MAC address is locally administered
    random_mac_str = ":".join("{:02x}".format(byte) for byte in random_mac)
    return random_mac_str


def generate_custom_mac(oui):
    device_mac = [random.randint(0x00, 0xff) for _ in range(3)]
    custom_mac = oui + ":" + ":".join("{:02x}".format(byte) for byte in device_mac)
    return custom_mac



def validate_mac(mac_address):
    if len(mac_address) != 17:
        return False
    components = mac_address.split(":")
    if len(components) != 6:
        return False
    try:
        for component in components:
            int(component, 16)
    except ValueError:
        return False
    return True

def restart_network_services():
    try:
        print(f"{Fore.BLUE}Restarting network services...{Style.RESET_ALL}")
        subprocess.check_call(["sudo", "service", "networking", "restart"])
        subprocess.check_call(["sudo", "service", "NetworkManager", "restart"])
        print(f"{Fore.MAGENTA}Network services have been restarted successfully.{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Failed to restart network services:{Style.RESET_ALL} {e}")

def change_mac(interface, new_mac):
    original_mac = get_original_mac(interface)
    print(f"{Fore.BLUE}{Style.BRIGHT}Changing MAC address{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Interface: {Style.RESET_ALL} {interface}")
    print(f"{Fore.GREEN}Old Mac  : {Style.RESET_ALL} {original_mac}")
    print(f"{Fore.GREEN}New Mac  : {Style.RESET_ALL} {new_mac}")
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print(f"{Fore.MAGENTA}MAC address changed successfully.{Style.RESET_ALL}")


def is_wireless_interface(interface):
    try:
        iwconfig_output = subprocess.check_output(["iwconfig", interface], stderr=subprocess.STDOUT, text=True)
        return 'no wireless extensions' not in iwconfig_output
    except subprocess.CalledProcessError:
        return False

def change_interface_mode(interface, mode):
    if not is_wireless_interface(interface):
        print(f"{Fore.RED}{interface}{Style.RESET_ALL} is not a wireless interface or not supported.")
        return False
    try:
        subprocess.check_call(["sudo", "ifconfig", interface, "down"])
        subprocess.check_call(["sudo", "iwconfig", interface, "mode", mode])
        subprocess.check_call(["sudo", "ifconfig", interface, "up"])
        print(f"Interface {Fore.GREEN}{interface}{Style.RESET_ALL} has been set to {Fore.GREEN}{mode}{Style.RESET_ALL} mode.")
        return True
    except:
        print(f"{Fore.RED}Error occurred while changing mode of {interface}{Style.RESET_ALL}")
        return False

def validate_interface(interface):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"{Fore.RED}Invalid interface:{Style.RESET_ALL} {interface}")  # Bold Red Text
        exit(1)



def main():
    parser = argparse.ArgumentParser(description='MacMaster: Mac Address Changer')
    parser.add_argument("--interface", "-i", help="Network interface to change MAC address")
    parser.add_argument("--list-interfaces", "-li", action="store_true", help="List all network interfaces")
    parser.add_argument("--version", "-V", action="store_true", help="Show the version of the program")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--random", "-r", action="store_true", help="Set a random MAC address")
    group.add_argument("--newmac", "-nm", type=str, help="Set a specific MAC address")
    group.add_argument("--customoui", "-co", type=str, help="Set a custom OUI for the MAC address")
    group.add_argument("--reset", "-rs", action="store_true", help="Reset MAC address to the original value")
    parser.add_argument("--mode", type=str, choices=['managed', 'monitor','master','auto','repeater'], help="Change interface mode to managed or monitor")
    parser.add_argument("--restart-network", "-rn", action="store_true", help="Restart network services")
    parser.add_argument("--monitor-mac-traffic", "-mmt", action="store_true", help="Live Monitor Mac traffic")


    args = parser.parse_args()

    if args.version:
        show_version()
        exit()
    if args.list_interfaces:
        list_network_interfaces()
        exit()
    if args.restart_network:
        restart_network_services()
        exit()
    if args.monitor_mac_traffic:
        start_traffic_monitoring(args.interface)

    if not args.interface:
        parser.print_help()
        exit()

    validate_interface(args.interface)
    save_original_mac(args.interface)

    if args.random:
        random_mac = generate_random_mac()
        change_mac(args.interface, random_mac)
    elif args.newmac:
        if validate_mac(args.newmac):
            change_mac(args.interface, args.newmac)
        else:
            print(f"{Fore.RED}Invalid MAC address format. Please provide a valid MAC address.{Style.RESET_ALL}")
    elif args.customoui:
        if validate_mac(args.customoui + ":00:00:00"):
            custom_mac = generate_custom_mac(args.customoui)
            change_mac(args.interface, custom_mac)
        else:
            print(f"{Fore.RED}Invalid OUI format. Please provide a valid OUI.{Style.RESET_ALL}")
    elif args.reset:
        original_mac = get_original_mac(args.interface)
        if original_mac:
            change_mac(args.interface, original_mac)
            print(f"{Fore.GREEN}MAC address reset to the original value{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Unable to reset the MAC address. Original MAC address not found.{Style.RESET_ALL}")

    if args.mode:
            success = change_interface_mode(args.interface, args.mode)
            if success:
                print(f"{Fore.GREEN}Mode change to {args.mode} was successful.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to change mode to {args.mode}.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
