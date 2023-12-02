import os
import re
import random
import argparse
import subprocess
from colorama import Fore, Style, init

init()  # Colorama'yı başlat


VERSION = "1.0.0"

def show_version():
    print(f"MacMaster Version: {VERSION}")


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



def validate_interface(interface):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"{Fore.RED}Invalid interface:{Style.RESET_ALL} {interface}")  # Bold Red Text
        exit(1)



def main():
    parser = argparse.ArgumentParser(description='MacMaster: Mac Address Changer')
    parser.add_argument("--interface", "-i", help="Network interface to change MAC address")
    parser.add_argument("--version", "-V", action="store_true", help="Show the version of the program")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--random", "-r", action="store_true", help="Set a random MAC address")
    group.add_argument("--newmac", "-nm", type=str, help="Set a specific MAC address")
    group.add_argument("--customoui", "-co", type=str, help="Set a custom OUI for the MAC address")
    group.add_argument("--reset", "-rs", action="store_true", help="Reset MAC address to the original value")
    args = parser.parse_args()

    if args.version:
        show_version()
        exit()

    if not args.interface:
        parser.error("the following arguments are required: --interface/-i")

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

if __name__ == "__main__":
    main()
