# 🔍 Network Scanner - Terminal Version

A powerful command-line network scanner for discovering devices on your network. Fast, efficient, and feature-rich with vendor identification and comprehensive error handling.


## ✨ Features

### 🔍 **Network Discovery**
- **ARP-based Scanning**: Fast and reliable device detection
- **Real-time Results**: See devices as they're discovered
- **Vendor Identification**: Automatic manufacturer lookup
- **Multiple IP Ranges**: Support for any network range

### ⚡ **Performance**
- **Fast Scanning**: Optimized for speed and efficiency
- **Configurable Timeout**: Adjust scan duration (1-60 seconds)
- **Progress Indicators**: Visual feedback during scanning
- **Memory Efficient**: Minimal resource usage

### 🛠️ **Advanced Features**
- **Command Line Interface**: Flexible CLI with multiple options
- **Error Handling**: Comprehensive validation and recovery
- **Cross-platform**: Works on Linux, macOS, and Windows
- **Privilege Checking**: Automatic permission verification

### 📊 **Output Options**
- **Formatted Tables**: Clean, readable results
- **Vendor Information**: Device manufacturer details
- **Statistics**: Scan timing and device counts
- **Verbose Mode**: Detailed debugging information

## 🚀 Quick Start

### **Installation**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the scanner
python main.py
```

### **Basic Usage**
```bash
# Scan default network (192.168.1.1/24)
python main.py

# Scan specific network
python main.py -r 10.0.0.1/24

# Set custom timeout
python main.py -t 3

# Enable verbose output
python main.py -v
```

## 🎯 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `-r, --range` | IP range to scan | `-r 192.168.1.1/24` |
| `-t, --timeout` | Timeout in seconds | `-t 5` |
| `-v, --verbose` | Enable verbose output | `-v` |
| `-h, --help` | Show help message | `-h` |

### **Examples**

```bash
# Quick scan of home network
python main.py

# Thorough scan with longer timeout
python main.py -r 192.168.0.1/24 -t 5

# Verbose scan for debugging
python main.py -r 10.0.0.1/24 -t 3 -v

# Scan corporate network
python main.py -r 172.16.1.1/24 -t 2
```

## 📊 Output Format

### **Standard Output**
```
[*] Initializing Network Scanner...
[*] Starting network scan...
[*] Target range: 192.168.1.1/24
[*] Timeout: 1 seconds
[*] Scanning network: 192.168.1.1/24 .....

================================================================================
NETWORK SCAN RESULTS - Found 5 device(s)
================================================================================
IP Address       MAC Address        Vendor                             
--------------------------------------------------------------------------------
192.168.1.1      00:11:22:33:44:55  Router Manufacturer
192.168.1.10     11:22:33:44:55:66  Apple Inc.
192.168.1.15     22:33:44:55:66:77  Samsung Electronics
192.168.1.20     33:44:55:66:77:88  Unknown
192.168.1.25     44:55:66:77:88:99  Microsoft Corporation
--------------------------------------------------------------------------------

============================================================
SCAN SUMMARY
============================================================
• Scan duration: 1.23 seconds
• Target range: 192.168.1.1/24
• Devices found: 5
• Scan status: Completed
============================================================
```

### **Verbose Output**
```
[*] Initializing Network Scanner...
[*] Validating IP range format...
[*] Checking network interface...
[*] Verifying network connectivity...
[*] Checking scanning privileges...
[*] Starting network scan...
[*] Target range: 192.168.1.1/24
[*] Timeout: 3 seconds
[*] Scanning network: 192.168.1.1/24 .....
[*] Old MAC: 00:11:22:33:44:55
[*] New MAC: 11:22:33:44:55:66
[+] MAC address changed successfully!
[+] Verification successful: 11:22:33:44:55:66
```

## 🔧 Advanced Usage

### **Common IP Ranges**
- `192.168.1.1/24` - Most home networks
- `192.168.0.1/24` - Alternative home networks
- `10.0.0.1/24` - Corporate networks
- `172.16.1.1/24` - Private networks

### **Timeout Guidelines**
- **1 second**: Fast scan (recommended for small networks)
- **3-5 seconds**: Thorough scan (recommended for most networks)
- **10+ seconds**: Comprehensive scan (for large or slow networks)

### **Error Handling**
The scanner includes comprehensive error handling for:
- Invalid IP ranges
- Network connectivity issues
- Permission problems
- API failures
- System errors

## ⚡ Performance Tips

### **Optimal Settings**
- **Small Networks** (< 50 devices): 1-2 second timeout
- **Medium Networks** (50-200 devices): 3-5 second timeout
- **Large Networks** (> 200 devices): 5-10 second timeout

### **Network Types**
- **Home Networks**: Usually fast, 1-2 second timeout
- **Corporate Networks**: May be slower, 3-5 second timeout
- **Public Networks**: Variable speed, 5-10 second timeout

## 🐛 Troubleshooting

### **Common Issues**

#### **"No devices found"**
```bash
# Check network connectivity
ping 192.168.1.1

# Try different IP range
python main.py -r 192.168.0.1/24

# Increase timeout
python main.py -t 5
```

#### **"Permission denied"**
```bash
# Run with administrator privileges
sudo python main.py

# On Windows, run as Administrator
python main.py
```

#### **"Invalid IP range"**
```bash
# Use correct format
python main.py -r 192.168.1.1/24

# Check your network range
ipconfig  # Windows
ifconfig  # Linux/macOS
```

#### **"Scan errors"**
```bash
# Check internet connection
ping 8.8.8.8

# Verify scapy installation
pip install scapy

# Try verbose mode for debugging
python main.py -v
```

### **Getting Help**
```bash
# Show help
python main.py -h

# Check version
python --version

# Verify dependencies
pip list | grep scapy
```

## 🔒 Security & Legal

### **Important Notes**
- **Only scan networks you own or have permission to scan**
- **Some networks may block or detect scans**
- **Use responsibly and legally**
- **Results depend on network configuration**

### **Best Practices**
- Test on your own network first
- Use appropriate timeouts to avoid network disruption
- Respect network policies and regulations
- Document your findings appropriately

## 📁 File Structure

```
network-scanner/
├── main.py             # Terminal-based scanner
├── gui_scanner.py      # GUI version
├── macChanger.py       # MAC address changer
├── requirements.txt    # Dependencies
└── README_terminal.md # This documentation
```

## 🛠️ Requirements

- **Python 3.6+**
- **Network privileges** (may require sudo/administrator)
- **Internet connection** (for vendor lookup)

### **Dependencies**
```
scapy>=2.4.5
requests>=2.25.1
```

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit your improvements

## 📄 License

This project is for educational purposes. Use responsibly and in accordance with local laws and network policies.

## 🙏 Acknowledgments

- **scapy**: Network packet manipulation
- **requests**: HTTP library for vendor lookup
- **macvendors.com**: MAC address vendor database
- **Python community**: Open source contributions

---

**Happy Scanning!** 🔍

*Remember: Always scan responsibly and only on networks you own or have permission to scan.* 
