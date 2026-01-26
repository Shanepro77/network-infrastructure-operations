This repository contains a Cisco Packet Tracer laboratory demonstrating the implementation of secure remote management for network infrastructure. By transitioning from unencrypted Telnet to SSH, this lab focuses on hardening the control plane and establishing secure administrative access.


Lab Features


-SVI Configuration: Implementation of a Switch Virtual Interface (SVI) on VLAN 1 for Layer 3 management.

-Asymmetric Encryption: Generation of RSA cryptokeys (1024-bit) to support SSHv2.

-Local Authentication: Configuration of local database users and VTY line security.

-Connectivity Validation: End-to-end testing using ICMP (Ping) and SSH client emulation.


Technical Skills Demonstrated


-Network Security: Replacing clear-text protocols with encrypted management sessions.

-Cisco IOS CLI: Proficiency in Global Configuration and Line Configuration modes.

-OSI Troubleshooting: Systematic resolution of connectivity issues across Layer 1 (Physical), Layer 2 (Data Link), and Layer 3 (Network).

-Device Hardening: Setting enable secret passwords and restricting transport input to SSH only.


 Lab Topology

 
-1x Multilayer switchSwitch (Management IP: 192.168.10.2

-1x Management Laptop (IP: 192.168.10.3)
-Cable: Copper Straight-Through
