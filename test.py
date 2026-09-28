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

target = input("Your Target(e.g example.com): ")

print("______________________NMAP TOOL______________________")

# Nmap version scan command

command = ["nmap", "-sV", "-p", "1-500", "-oN", "Fullscan.txt", target]

result = subprocess.run(command, capture_output=True, text=True)

print("PORT    STATE SERVICE        VERSION")

for port in ("21", "80", "443"):
    m = re.search(rf"^{port}/tcp\s+.*$", result.stdout)
    if m:
        print(m.group(0))
    else:
        print(f"{port}/tcp  closed/filtered or not found")
        
        print("Full scan saved in Fullscan.txt")

print("______________________SUBFINDER TOOL______________________")

# Subfinder enumerate Command:

command2 = ["subfinder","-d", target,"-o","subdomain.txt"]

print(subprocess.run(command2,capture_output=True, text=True).stdout)

with open("subdomain.txt") as f:
    print(f.read())




