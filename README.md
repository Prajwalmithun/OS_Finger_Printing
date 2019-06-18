# OS_Finger_Printing
This project mainly encompasses on determining the operating system of the specific host in the network that it is connected to.

## Getting Started
  ### Prerequisite
  ```
  python-nmap
  nmap
  ```
  ### Installation
  Installing the Prerequisites
  #### Fedora
  ```
  $ pip install python-nmap
  $ sudo yum install nmap
  ```
  #### Debian or Ubuntu
  ```
  $ pip install python-nmap
  $ sudo apt-get install nmap
  ```
  ## Running
  ```
  $ git clone https://github.com/Prajwalmithun/OS_Finger_Printing.git
  $ cd OS_Finger_Printing
  $ python3 scanner.py [ip_address of the host]
  $ vi osinfo.txt
  ```
  This "osinfo.txt" file contains the information about the operating system, ports that are open.
