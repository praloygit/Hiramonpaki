import subprocess
import re

banner = r"""
             _   _ ___ ____      _    __  __  ___  _   _
            | | | |_ _|  _ \    / \  |  \/  |/ _ \| \ | |
            | |_| || || |_) |  / _ \ | |\/| | | | |  \| |
            |  _  || ||  _ <  / ___ \| |  | | |_| | |\  |
            |_| |_|___|_| \_\/_/   \_\_|  |_|\___/|_| \_|
            
                            .*###@@@@###*.
                      *#@@@@@@@@@@@@@@@@@@@@@@#*
                 .#@@@@@@@@#@@@@@@@@@@@@@* .**#@@@@#.
              *@@@@@@#*  .@@@@@@#****#@@@@@@.      *#@#*
           #@@@@@#.     #@@@#.          .#@@@#         ***.
        *@@@@@*        #@@@           *#@@@@@@#
      #@@@@#          *@@@      .*@@@@@@@@#*
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.     .@@@@@@@@@@@@##########
  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*          *@@@@@@@@@@@@@@@@@@@@@.
                      #@@@                  @@@#          .@@@@@.
                      .@@@*                *@@@         #@@@@@.
           .*.          @@@@*            *@@@@.     .#@@@@@#
             *##*.       *@@@@#*      *#@@@@*   .*@@@@@@*
                *#@@@#*    *@@@@@@@@@@@@@@#*#@@@@@@@#*
                    *#@@@@@@@@#@@@@@@@@@@@@@@@@@#.
                         .*##@@@@@@@@@@@@##*.
                      ____   _    _  ___   _ ___
                     |  _ \ / \  | |/ / | | |_ _|
                     | |_) / _ \ | ' /| |_| || |
                     |  __/ ___ \| . \|  _  || |
                     |_| /_/   \_\_|\_\_| |_|___|
"""
 
print("\033[1;36m" + banner + "\033[0m")

CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"

target = input(f"{RED}Your Target{RESET}({YELLOW}e.g example.com{RESET}): ")



print(f"______________________{CYAN}NMAP TOOL{RESET}______________________")

# Nmap version and port scan command

command = ["nmap", "-sV", "-p", "1-500", "-oN", "Fullscan.txt", target]

print(f"{YELLOW}Running nmap scan... please wait{RESET}")

result = subprocess.run(command, capture_output=True, text=True)

print("| PORT | STATE | SERVICE | VERSION |")

for port in ("21", "80", "443"):
    match = re.search(rf"^{port}/tcp\s+.*$", result.stdout, re.MULTILINE)
    if match:
        print(match.group(0))
    else:
        print(f"{port}/tcp  closed/filtered or not found")

print(f"{GREEN}nmap finished.{RESET}")       

print(f"{GREEN}Full nmap scan saved in {RED}{"Fullscan.txt"}{RESET}{RESET}")



print(f"______________________{CYAN}SUBFINDER TOOL{RESET}______________________")

# Subfinder enumerate Command:

command2 = ["subfinder","-d", target, "-silent", "-o","subdomain.txt"]

print(f"{YELLOW}Running subfinder scan... please wait{RESET}")

print(subprocess.run(command2,capture_output=True, text=True).stdout)

print(f"{GREEN}subfinder finished.{RESET}")

print(f"{GREEN}Subdomain scan saved in {RED}subdomains.txt{RESET}{RESET}")
