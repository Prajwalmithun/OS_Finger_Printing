# OS_Finger_Printing

This project mainly encompasses on determining the operating system of the specific host in the network that it is connected to.
It is not only specific to determine the OS but also gives the status of host with opened ports.
It is one of the methods under Active Information Gathering under the PTES(ie.,Penetration Testing Execution Standard). 
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
  $ sudo python3 scanner.py [ip_address of the host]
  $ vi osinfo.txt
  ```
  This "osinfo.txt" file contains the information about the operating system, ports that are open.
