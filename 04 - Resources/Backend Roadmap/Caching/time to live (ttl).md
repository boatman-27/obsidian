Time to live (TTL) refers to the amount of time or “hops” that a packet is set to exist inside a network before being discarded by a router.

## How does TTL work?

When a packet of information is created and sent out across the Internet, there is a risk that it will continue to pass from router to router indefinitely. To mitigate this possibility, packets are designed with an expiration called a time-to-live or hop limit. Packet TTL can also be useful in determining how long a packet has been in circulation, and allow the sender to receive information about a packet’s path through the Internet.

Each packet has a place where it stores a numerical value determining how much longer it should continue to move through the network. Every time a router receives a packet, it subtracts one from the TTL count and then passes it onto the next location in the network. If at any point the TTL count is equal to zero after the subtraction, the router will discard the packet and send an [ICMP message](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/) back to the originating host.

In the context of a [DNS record](https://www.cloudflare.com/learning/dns/dns-records/), TTL is a numerical value that determines how long a DNS cache server can serve a DNS record before reaching out to the authoritative DNS server and getting a new copy of the record.