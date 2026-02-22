```
__        _____  ____  ____  ____  ____  _____ ____ ____  
\ \      / / _ \|  _ \|  _ \|  _ \|  _ \| ____/ ___/ ___| 
 \ \ /\ / / | | | |_) | | | | |_) | |_) |  _| \___ \___ \ 
  \ V  V /| |_| |  _ <| |_| |  _ <|  _ <| |___ ___) |__) |
   \_/\_/  \___/|_| \_\____/|_| \_\_| \_\_____|____/____/ 
```
WORDPRESS-SCANNER
A fast and efficient Python-based automation tool for scanning WordPress websites. 
It simplifies the use of WPScan by providing a user-friendly menu to identify 
vulnerabilities, plugins, themes, and administrative usernames.

**Features**
* **Fast Scan:** Performs a standard security scan on the target WordPress URL.
* **Plugin Scan:** Enumerates all detected plugins to find outdated or vulnerable ones.
* **Theme Scan:** Specifically looks for active themes and their potential security flaws.
* **User Enumeration:** Attempts to identify valid administrative usernames for security auditing.
* **Automated Setup:** Automatically checks and installs 'figlet' for the best visual experience.

**Prerequisites**
The following tools are required for the script to function:
* Python 3.x
* WPScan: The core scanning engine (Must be installed on your system).
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/WordPress-Scanner.git

Navigate to the directory:
   * cd WordPress-Scanner

Make the script executable:
   * chmod +x wp_scanner.py

**Usage**
Since network scanning and package installation may require elevated permissions, it is recommended to run with sudo:

sudo python3 wp_scanner.py

**Menu Options:**
1. Fast Scan: Quick overview of the target site's security.
2. Plugin Scan: Detailed list of installed WordPress plugins.
3. Theme Scan: Analysis of the themes used by the target.
4. Admin Username Scan: Enumerates users to test for brute-force vulnerability.

**Important Notes:**
* Figlet: Used for the ASCII header display.
* Root Privileges: Required for automated dependency installation and optimal performance.
* Ethics: Only use this tool on systems you own or have explicit permission to test.
