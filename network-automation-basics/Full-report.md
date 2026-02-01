# Network Automation Lab (Conceptual – Cisco IOS)

## Overview
This lab demonstrates **network automation design** using Python and Netmiko to automate common Cisco IOS operational checks over SSH. The focus is on **design intent, workflow, and safety**, not execution within a simulator.

The automation mirrors manual CLI workflows already validated in prior networking labs.

---

## Objectives
- Demonstrate how SSH-based automation would interact with Cisco IOS devices
- Translate common operational CLI checks into repeatable automation
- Apply a **read-first, non-disruptive automation approach**
- Show design readiness for real-device environments (NOC / Junior Network roles)

---

## Environment & Assumptions
- Cisco IOS switches and routers
- Management access via SSH to a **management SVI**
- Automation executed from an administrator workstation or jump host
- Packet Tracer used for **topology and command validation only**

> **Note:** Automation scripts are provided as **design artifacts**.  
> Execution requires real or emulated IOS devices (e.g. DevNet or GNS3) and is outside the scope of this lab.

---

## Design Approach
Manual network configuration and troubleshooting were completed first using the Cisco CLI.  
Automation was then designed to **replicate the same operational visibility programmatically**, ensuring consistency and reducing manual repetition.

Automation is intentionally scoped to **read-only commands** to prioritise safety and auditability.

---

## Automation Workflow (Conceptual)
1. Establish an SSH session to the device management SVI
2. Execute predefined operational commands
3. Collect and return live network state
4. Close the session cleanly

This reflects common operational use cases such as:
- Network audits
- Pre-change validation
- Troubleshooting support

---

## Automation Artifacts
The following files represent the automation design used in this lab:

get-vlan-brief.py
The script is executed manually by an administrator to automatically collect VLAN state via SSH.

get-device-state.py – Conceptual script to collect interface, trunk, and routing status
sample-output.txt – Illustrative example of returned command output


These artifacts demonstrate **how automation would be implemented** against real devices.

---

## Automated Command Coverage
The automation targets commands commonly used in daily operations:

```ios
show vlan brief
show ip interface brief
show interfaces trunk
show ip route
```
These commands provide visibility into switching, routing, and inter-VLAN connectivity.

## Validation Logic
Successful automation execution would:

Return accurate VLAN membership and port assignments

Reflect correct SVI and interface states

Show expected trunk and routing information

Match the results of manual CLI verification
