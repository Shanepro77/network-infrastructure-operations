## Troubleshooting & Lessons Learned

### 1. SSH Connectivity Failure After Routing Changes
**Issue:** SSH access failed after enabling inter-VLAN routing and trunking.  
**Root Cause:** Management SVI IP mismatch and altered traffic flow once Layer 3 routing was enabled.  
**Resolution:** Verified correct SVI using `show ip interface brief` and corrected default gateway alignment.  
**Lesson:** Enabling routing changes management plane traffic paths. Always validate gateway logic after topology changes.

---

### 2. VLAN Interface Up/Down State
**Issue:** SVI showed `up/down` status.  
**Root Cause:** No active access port assigned to the VLAN.  
**Resolution:** Assigned an active port to the VLAN and confirmed link state.  
**Lesson:** An SVI becomes fully operational only when at least one port in that VLAN is active.

---

### 3. SSH Timeout Errors
**Issue:** `% Connection timed out; remote host not responding`  

**Root Causes Identified:**
- Incorrect SVI IP
- VLAN mismatch
- Missing routing between VLANs
- Incorrect PC default gateway
- Interface administratively down

**Lesson:** SSH failures are usually Layer 2 or Layer 3 problems, not SSH configuration issues.

---

### 4. Missing `no shutdown`
**Issue:** Configured SVI unreachable.  
**Root Cause:** Interface administratively down.  
**Resolution:** Applied `no shutdown` and validated operational state.  
**Lesson:** Always verify interface status after configuration.

---

### 5. Default Gateway Misalignment
**Issue:** Inconsistent connectivity between PC and switch.  
**Root Cause:** Incorrect default gateway configured on client.  
**Resolution:** Corrected gateway to match VLAN SVI.  
**Lesson:** End devices must use the SVI of their VLAN as the default gateway when routing is enabled.

---

### 6. VLAN Assignment Confusion
**Issue:** Misinterpretation of management VLAN versus access VLAN.  
**Lesson:** Management plane traffic must reside within the same VLAN or be properly routed. Clear separation between access and management design is essential.

---

### 7. Verification Discipline Improvement
Frequent issues were resolved faster after consistently using:

- `show ip interface brief`
- `show vlan brief`
- `show interfaces trunk`
- `show ip route`
- `show running-config`

**Lesson:** Always validate current device state before modifying configuration.
