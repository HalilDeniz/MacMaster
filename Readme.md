# MacMaster : MAC Address Changer

MacMaster : MAC Address Changer is a command line tool that allows you to change the MAC address of a network interface on your system.

## Features

- Set a specific MAC address.
- Generate and set a random MAC address.
- Reset MAC address to its original value.

## Usage

You can use the MAC Address Changer in three ways:

1. Set a specific MAC address:

```bash
python3 macmaster.py -i eth0 -nm 00:11:22:33:44:55
```

2. Set a random MAC address:

```bash
python3 macmaster.py -i eth0 -r
```

3. Reset MAC address to its original value:

```bash
python3 macmaster.py -i eth0 -rs
```

Where `eth0` is your network interface.

## Arguments

- `--interface` or `-i` : Specify the network interface.
- `--random` or `-r` : Set a random MAC address.
- `--newmac` or `-nm` : Set a specific MAC address.
- `--reset` or `-rs` : Reset MAC address to the original value.

## Note

You must run this script as root or use sudo to run this script for it to work properly. This is because changing a MAC address requires root privileges.

## Future Enhancements

We're always open to improvements and new feature ideas. Please feel free to submit a pull request or open an issue for discussion.


## Contributing
Contributions are welcome! To contribute to MacMaster, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in the main repository.



## Contact

For any inquiries or further information, you can reach me through the following channels:

- LinkedIn: [Halil Ibrahim Deniz](https://www.linkedin.com/in/halil-ibrahim-deniz/)
- TryHackMe: [Halilovic](https://tryhackme.com/p/halilovic)
- Instagram: [deniz.halil333](https://www.instagram.com/deniz.halil333/)
- YouTube: [Halil Deniz](https://www.youtube.com/c/HalilDeniz)
- Email: halildeniz313@gmail.com

## License

Mac-MacMaster is released under the MIT License. See LICENSE for more information.
