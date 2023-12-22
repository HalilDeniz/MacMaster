# MacMaster: Advanced Network Interface Management and Monitoring

MacMaster is a comprehensive command-line tool crafted for network professionals and enthusiasts alike. It stands out as a powerful utility for manipulating the MAC addresses of network interfaces on various systems. Designed with both simplicity and functionality in mind, MacMaster excels in providing solutions for enhancing network anonymity, conducting security tests, and performing a wide range of network diagnostics and monitoring tasks. Whether you're looking to anonymize your network presence, troubleshoot connectivity issues, or engage in advanced network analysis, MacMaster equips you with the tools necessary to accomplish these tasks efficiently.


## Features

- **Custom MAC Address:** Set a specific MAC address to your network interface.
- **Random MAC Address:** Generate and set a random MAC address.
- **Reset to Original:** Reset the MAC address to its original hardware value.
- **Custom OUI:** Set a custom Organizationally Unique Identifier (OUI) for the MAC address.
- **Version Information:** Easily check the version of MacMaster you are using.
- **Network Interface Listing:** Easily list all available network interfaces.
- **Interface Mode Switching:** Switch wireless network interfaces between 'managed' and 'monitor' modes.
- **Network Services Reset:** Quickly reset networking services to apply changes or troubleshoot.
- **Network Traffic Monitoring:** Monitor MAC traffic in real-time for analysis and security testing.

## **Installation**
MacMaster requires Python 3.6 or later.

1. Clone the repository:
    ```bash
    $ git clone https://github.com/HalilDeniz/MacMaster.git
    ```
2. Navigate to the cloned directory:
   ```bash
   cd MacMaster
   ```
2. Install the package:
    ```bash
    $ python setup.py install
    ```


## Usage
```bash
$ macmaster.py --help
usage: macmaster.py [-h] [--interface INTERFACE] [--list-interfaces] [--version]
                    [--random | --newmac NEWMAC | --customoui CUSTOMOUI | --reset]
                    [--mode {managed,monitor,master,auto,repeater}] [--get-ssid] [--check-security]
                    [--analyze-signal] [--restart-network] [--monitor-mac-traffic] [--analyze-packets]

MacMaster: Advanced Network Interface Management and Monitoring

options:
  -h, --help            show this help message and exit
  --interface INTERFACE, -i INTERFACE
                        Network interface to change MAC address
  --list-interfaces, -li
                        List all network interfaces
  --version, -V         Show the version of the program
  --random, -r          Set a random MAC address
  --newmac NEWMAC, -nm NEWMAC
                        Set a specific MAC address
  --customoui CUSTOMOUI, -co CUSTOMOUI
                        Set a custom OUI for the MAC address
  --reset, -rs          Reset MAC address to the original value
  --mode {managed,monitor,master,auto,repeater}
                        Change interface mode to managed or monitor
  --get-ssid            Get the SSID of the wireless interface
  --check-security      Check the security protocol of the wireless interface
  --analyze-signal      Analyze the signal strength and quality of the wireless interface
  --restart-network, -rn
                        Restart network services
  --monitor-mac-traffic, -mmt
                        Live Monitor Mac traffic
  --analyze-packets, -ap
                        Analyze network packets on the interface
```

## Arguments
- `--interface`, `-i`: Specify the network interface to be used for MAC address operations.
- `--random`, `-r`: Generate and set a random MAC address on the specified interface.
- `--newmac`, `-nm`: Set a specific MAC address on the specified interface.
- `--customoui`, `-co`: Set a custom Organizationally Unique Identifier (OUI) for the MAC address on the specified interface.
- `--reset`, `-rs`: Reset the MAC address of the specified interface to its original hardware value.
- `--version`, `-V`: Show the current version of MacMaster.
- `--list-interfaces`, `-li`: List all network interfaces available on the system.
- `--mode`, `-m`: Change the mode of a wireless network interface (options include 'managed', 'monitor', 'master', 'auto', 'repeater').
- `--restart-network`, `-rn`: Restart network services to apply changes or troubleshoot network issues.
- `--monitor-mac-traffic`, `-mmt`: Monitor and display MAC traffic in real-time on the specified interface.
- `--get-ssid`, `-gs`: Display the SSID of the connected Wi-Fi network.
- `--analyze-signal`, `-as`: Analyze the signal strength and quality of the wireless interface.
- `--check-security`, `-cs`: Check the security protocol of the wireless interface.
- `--analyze-packets`, `-ap`: Analyze network packets on the interface.

### Examples

1. **Set a specific MAC address:**
   ```bash
   macmaster -i eth0 -nm 00:11:22:33:44:55
   ```
2. **Set a random MAC address:**
   ```bash
   macmaster -i eth0 -r
   ```
3. **Reset MAC address to its original value:**
   ```bash
   macmaster -i eth0 -rs
   ```
4. **List all network interfaces:**
   ```bash
   macmaster -li
   ```
5. **Change interface mode:**
   ```bash
   macmaster -i eth0 -m monitor
   ```
6. **Restart network services:**
   ```bash
   macmaster -rn
   ```
7. **Monitor MAC traffic in real-time:**
   ```bash
   macmaster -i eth0 -mmt
   ```

## Note

You must run this script as root or use sudo to run this script for it to work properly. This is because changing a MAC address requires root privileges.

## Contributing
Contributions are welcome! To contribute to MacMaster, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in the main repository.


## Contact

For any inquiries or further information, you can reach me through the following channels:

## Contact
- Linktr :[Halil Deniz](https://linktr.ee/halildeniz)
- LinkedIn  : [Halil İbrahim Deniz](https://www.linkedin.com/in/halil-ibrahim-deniz/)
- TryHackMe : [halilovic](https://tryhackme.com/p/halilovic)
- Instagram : [deniz.halil333](https://www.instagram.com/deniz.halil333/)
- YouTube   : [HalilDeniz](https://www.youtube.com/c/HalilDeniz)
- Email: halildeniz313@gmail.com
## License

MacMaster is released under the MIT License. See [LICENSE](LICENSE) for more information.
