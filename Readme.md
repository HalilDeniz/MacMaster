# MacMaster: MAC Address Changer

MacMaster is a versatile command line tool designed to change the MAC address of network interfaces on your system. It provides a simple yet powerful solution for network anonymity and testing.

## Features

- **Custom MAC Address:** Set a specific MAC address to your network interface.
- **Random MAC Address:** Generate and set a random MAC address.
- **Reset to Original:** Reset the MAC address to its original hardware value.
- **Custom OUI:** Set a custom Organizationally Unique Identifier (OUI) for the MAC address.
- **Version Information:** Easily check the version of MacMaster you are using.


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
$ macmaster --help         
usage: macmaster [-h] [--interface INTERFACE] [--version]
                 [--random | --newmac NEWMAC | --customoui CUSTOMOUI | --reset]

MacMaster: Mac Address Changer

options:
  -h, --help            show this help message and exit
  --interface INTERFACE, -i INTERFACE
                        Network interface to change MAC address
  --version, -V         Show the version of the program
  --random, -r          Set a random MAC address
  --newmac NEWMAC, -nm NEWMAC
                        Set a specific MAC address
  --customoui CUSTOMOUI, -co CUSTOMOUI
                        Set a custom OUI for the MAC address
  --reset, -rs          Reset MAC address to the original value
```
## Arguments

- `--interface`, `-i`: Specify the network interface.
- `--random`, `-r`: Set a random MAC address.
- `--newmac`, `-nm`: Set a specific MAC address.
- `--customoui`, `-co`: Set a custom OUI for the MAC address.
- `--reset`, `-rs`: Reset MAC address to the original value.
- `--version`, `-V`: Show the version of the program.


1. **Set a specific MAC address:**
   ```bash
   $ macmaster.py -i eth0 -nm 00:11:22:33:44:55
   ```
2. **Set a random MAC address:**
   ```bash
   $ macmaster.py -i eth0 -r
   ```
3. **Reset MAC address to its original value:**
   ```bash
   $ macmaster.py -i eth0 -rs
   ```
4. **Set a custom OUI:**
   ```bash
   $ macmaster.py -i eth0 -co 08:00:27
   ```
5. **Show program version:**
   ```bash
   $ macmaster.py -V
   ```
Replace `eth0` with your desired network interface.

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
