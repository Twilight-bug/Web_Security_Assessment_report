import os
import subprocess

# Local target subnet mask range to audit
target_subnet = "192.168.1.0/24" # Adjust to match your local IP schema

print(f"[*] Commencing automated Enterprise SMB Security Audit on: {target_subnet}\n")

try:
    # Use nmap programmatically to scan for disabled SMB signing
    cmd = f"nmap -p 445 --script smb-security-mode {target_subnet}"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    clean_output = output.decode('utf-8')
    lines = clean_output.split('\n')
    
    for line in lines:
        if "Nmap scan report for" in line:
            print(f"\n[+] Active Host Spotted: {line.replace('Nmap scan report for ', '')}")
        if "message_signing: disabled" in line or "required: false" in line:
            print(f" [!] SECURITY ALERT: SMB Message Signing is NOT required! (Vulnerable to NTLM Relay Attacks)")
            
except Exception as e:
    print(f"[!] Error executing network scanner script: {e}")
