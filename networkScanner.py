#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import sys
import time
import threading
from typing import List, Dict, Optional
import requests

def get_vendor_info(mac_address: str) -> str:
    """Get vendor information for a MAC address using macvendors.com API"""
    try:
        # Remove colons and convert to uppercase
        mac_clean = mac_address.replace(':', '').upper()
        url = f"https://api.macvendors.com/{mac_clean}"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown"
    except:
        return "Unknown"

def scan(ip_range: str, timeout: int = 1, verbose: bool = False) -> List[Dict[str, str]]:
    # Global flag to control loading animation
    loading_stop = threading.Event()
    
    def loading_animation():
        """Display loading dots while scanning"""
        while not loading_stop.is_set():
            # Show dots one by one
            for i in range(5):
                dots = "." * (i + 1) + " " * (4 - i)
                print(f"\r[*] Scanning network: {ip_range} {dots}", end='', flush=True)
                time.sleep(0.2)
            # Hide dots one by one
            for i in range(4, -1, -1):
                dots = "." * i + " " * (5 - i)
                print(f"\r[*] Scanning network: {ip_range} {dots}", end='', flush=True)
                time.sleep(0.2)
        print()  # New line after loading stops
    
    try:
        print(f"[*] Timeout: {timeout} seconds")
        
        # Start loading animation in a separate thread
        if not verbose:
            loading_thread = threading.Thread(target=loading_animation)
            loading_thread.daemon = True
            loading_thread.start()
        
        # Create ARP request packet
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        
        # Send packets and capture responses
        answered_list = scapy.srp(arp_request_broadcast, timeout=timeout, verbose=verbose)[0]
        
        # Stop loading animation
        loading_stop.set()
        
        clients_list = []
        for element in answered_list:
            ip = element[1].psrc
            mac = element[1].hwsrc
            
            # Get vendor information
            vendor = get_vendor_info(mac)
            
            client_dict = {
                "ip": ip,
                "mac": mac,
                "vendor": vendor
            }
            clients_list.append(client_dict)
            
        return clients_list
        
    except Exception as e:
        # Stop loading animation on error
        loading_stop.set()
        print(f"[!] Error during network scan: {e}")
        return []

def print_result(results_list: List[Dict[str, str]]) -> None:
    
    if not results_list:
        print("[!] No devices found on the network")
        return
    
    print("\n" + "="*80)
    print(f"NETWORK SCAN RESULTS - Found {len(results_list)} device(s)")
    print("="*80)
    print(f"{'IP Address':<16} {'MAC Address':<18} {'Vendor':<35}")
    print("-" * 80)
    
    for client in results_list:
        ip = client["ip"]
        mac = client["mac"]
        vendor = client["vendor"]
        
        # Truncate vendor name if too long
        if len(vendor) > 32:
            vendor = vendor[:29] + "..."
        
        print(f"{ip:<16} {mac:<18} {vendor:<35}")
    
    print("-" * 80)

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Network Scanner - Discover devices on your network",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Scan default network (192.168.1.1/24)
  python main.py -r 10.0.0.1/24    # Scan specific network
  python main.py -t 3               # Set timeout to 3 seconds
  python main.py -v                 # Verbose output
        """
    )
    
    parser.add_argument(
        "-r", "--range",
        dest="ip_range",
        default="192.168.1.1/24",
        help="IP range to scan (default: 192.168.1.1/24)"
    )
    
    parser.add_argument(
        "-t", "--timeout",
        dest="timeout",
        type=int,
        default=1,
        help="Timeout for each ARP request in seconds (default: 1)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        dest="verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    return parser.parse_args()

def main() -> None:
    """Main function"""
    try:
        # Parse command line arguments
        args = get_args()
        
        # Check if running with appropriate privileges
        if not scapy.conf.iface:
            print("[!] Warning: No network interface detected")
        
        # Perform network scan
        start_time = time.time()
        scan_result = scan(args.ip_range, args.timeout, args.verbose)
        scan_time = time.time() - start_time
        
        # Print results
        print_result(scan_result)
        
        # Print summary
        print(f"\n[*] Scan completed in {scan_time:.2f} seconds")
        print(f"[*] Scanned range: {args.ip_range}")
        
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()