# Mac Address Changer

The Mac Address Changer is a command-line tool designed to change the MAC address of a network interface. It provides a simple and convenient way to modify the MAC address for privacy, security, or network testing purposes.

## Features

- Change the MAC address of a specific network interface.
- Set a random MAC address for the interface.
- Specify a specific MAC address to assign to the interface.
- Verify and validate MAC address format.
- Reset the interface to its original MAC address.

## Installation

To install Mac Address Changer, you can simply clone the repository from GitHub:

```
git clone https://github.com/HalilDeniz/MacChanger.git
```
## Getting Started

To start using the Mac Address Changer tool, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the tool is installed.
3. Run the following command to view the help menu:

```
┌──(root💀denizhalil)-[~/PycharmProjects/pythonProject1]
└─# python3 mac_changer.py --help
usage: mac_changer.py [-h] --interface INTERFACE (--random | --newmac NEWMAC | --reset)

Mac Address Changer

options:
  -h, --help            show this help message and exit
  --interface INTERFACE, -i INTERFACE
                        Network interface to change MAC address
  --random, -r          Set a random MAC address
  --newmac NEWMAC, -nm NEWMAC
                        Set a specific MAC address
  --reset, -rs          Reset MAC address to the original value

Example Uses:
            python3 mac_changer.py -i eth0 -r
            python3 mac_changer.py -i eth0 --reset
            python3 mac_changer.py -i wlan0 -nm 00:11:22:33:44:55
```

4. Review the available options and commands.
5. Use the appropriate command to change the MAC address based on your requirements.

## Usage Examples

Here are some usage examples of the Mac Address Changer tool:

```
# Set a random MAC address for the "eth0" interface
1) python3 mac_changer.py -i eth0 -r

# Assign a specific MAC address (00:11:22:33:44:55) to the "wlan0" interface
2) python3 mac_changer.py -i wlan0 -nm 00:11:22:33:44:55

# For the original mac address of the system
3) python3 mac_changer.py -i eth0 --reset
```

Make sure to replace "eth0" and "wlan0" with the actual names of your network interfaces.

## Contact

For any inquiries or further information, you can reach me through the following channels:

- LinkedIn: [Halil Ibrahim Deniz](https://www.linkedin.com/in/halil-ibrahim-deniz/)
- TryHackMe: [Halilovic](https://tryhackme.com/p/halilovic)
- Instagram: [deniz.halil333](https://www.instagram.com/deniz.halil333/)
- YouTube: [Halil Deniz](https://www.youtube.com/c/HalilDeniz)
- Email: halildeniz313@gmail.com

## License

Mac-changer is released under the MIT License. See LICENSE for more information.