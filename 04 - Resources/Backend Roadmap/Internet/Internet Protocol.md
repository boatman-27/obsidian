## Internet Protocol (IP)
An Internet Protocol address (IP address) is a numerical label such as `192.0.2.1` assigned to devices on a network that uses IP for communication.
### Functions
- **Network interface identification**: Each device on a network has a unique IP address.
- **Location addressing**: Allows devices to locate and communicate with each other across networks.
### structure
- **IPv4**: Consists of 32 bits, typically displayed as four 8-bit numbers separated by dots (e.g., `192.168.1.1`).
    - First 8 bits: Country/network
    - Next 8 bits: Region
    - Next 8 bits: Subnetwork
    - Last 8 bits: Device
- **IPv6**: Consists of 128 bits, allowing for approximately 340 undecillion unique addresses, supporting the growing number of internet-connected devices.
## Domain Name System (DNS)
DNS is the system that translates human-readable domain names (like `www.example.com`) into IP addresses that computers use to identify each other on the network.

DNS servers distributed worldwide work together to resolve user queries, forming a global directory service. The system uses a tree-like structure with root servers at the top, followed by top-level domain servers (.com, .org, etc.), authoritative name servers for specific domains, and local DNS servers.
### How It Works
- When a user enters a URL in a browser, the DNS server is queried.
- The DNS server returns the corresponding IP address.
- The browser uses the IP address to connect to the target server and load the website.
### Importance
- **User-friendly navigation**: Users don’t need to memorize IP addresses.
- **Flexible website management**: Domains can point to different IPs as servers change.
- **Scalability**: Supports millions of domains and websites.