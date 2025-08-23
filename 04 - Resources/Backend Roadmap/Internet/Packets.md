## Packets
When data is sent over the internet, it is broken into small units called **packets**.
### Structure of a Packet
- **Header**: Contains source and destination IP addresses, packet number, and protocol information.
- **Payload**: The actual data being transmitted.
- **Footer** (optional): May include error-checking information.
### Why Use Packets?
- Efficient and manageable data transfer
- Enables error detection and correction
- Supports reassembly in correct order on the receiving end
## Routing
Routing is the process of determining the path that a packet takes to reach its destination.
### How It Works
- Each packet may take a different route through routers on the internet.
- Routers examine the packet header and forward it based on the best available path.

## Reliability
The internet is designed for fault tolerance and reliable communication.

### TCP vs UDP
- **TCP (Transmission Control Protocol)**: Ensures reliable delivery through acknowledgments and retransmission
- **UDP (User Datagram Protocol)**: Faster but does not guarantee delivery
### Mechanisms for Reliability
- **Acknowledgments (ACKs)**: Sender waits for confirmation of receipt
- **Retransmission**: Lost or corrupted packets are resent

These components work together to ensure that information can travel efficiently and accurately across networks, regardless of the underlying medium (Ethernet, fiber, or wireless).