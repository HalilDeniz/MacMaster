import argparse
import random
import re
import subprocess
import os


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
    print("\033[1;34m   Changing MAC address\033[0m")  # Bold Blue Text
    print("\033[1;32mInterface:\033[0m", interface)  # Bold Green Text
    print("\033[1;32mNew Mac:\033[0m", new_mac)  # Bold Green Text
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("\033[1;35mMAC address changed successfully.\033[0m")  # Bold Magenta Text


def validate_interface(interface):
    result = subprocess.run(["ifconfig", interface], capture_output=True, text=True)
    if result.returncode != 0:
        print("\033[1;31mInvalid interface:\033[0m", interface)  # Bold Red Text
        exit(1)



def main():
    parser = argparse.ArgumentParser(description='Mac Address Changer',
                                     epilog='''Example Uses:
            python3 mac_changer.py -i eth0 -r
            python3 mac_changer.py -i eth0 --reset
            python3 mac_changer.py -i wlan0 -nm 00:11:22:33:44:55
            ''', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--interface", "-i", required=True, help="Network interface to change MAC address")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--random", "-r", action="store_true", help="Set a random MAC address")
    group.add_argument("--newmac", "-nm", type=str, help="Set a specific MAC address")
    group.add_argument("--reset", "-rs", action="store_true", help="Reset MAC address to the original value")
    args = parser.parse_args()

    validate_interface(args.interface)
    save_original_mac(args.interface)

    if args.random:
        random_mac = generate_random_mac()
        change_mac(args.interface, random_mac)
    elif args.newmac:
        new_mac = args.newmac
        if validate_mac(new_mac):
            change_mac(args.interface, new_mac)
        else:
            print("\033[1;31mInvalid MAC address format. Please provide a valid MAC address.\033[0m")
    elif args.reset:
        original_mac = get_original_mac(args.interface)
        if original_mac:
            change_mac(args.interface, original_mac)
            print("\033[1;32mMAC address reset to the original value.\033[0m")
        else:
            print("\033[1;31mUnable to reset the MAC address. Original MAC address not found.\033[0m")


if __name__ == "__main__":
    main()
