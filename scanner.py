import nmap
import sys
from datetime import datetime

#Initiating the port scanner
nm_scanner=nmap.PortScanner()

print("Running...\n")
#Scanning
#argv[1] holds the IP address of the host
#'80' is the port address
#-O indicates OSprinting
nm_scan=nm_scanner.scan(sys.argv[1],'80',arguments='-O')

host_is_up="The host is:"+ nm_scan['scan'][sys.argv[1]]['status']['state']+".\n"
port_open="Port 80 is:"+ nm_scan['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
method_scan="Scanning method is:"+nm_scan['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
predicted_os="Predicted Operating System is:"+nm_scan['scan'][sys.argv[1]]['osmatch'][0]['osclass'][0]['osfamily']+".\n"
prediction_per="OS Prediction percentage is :"+nm_scan['scan'][sys.argv[1]]['osmatch'][0]['accuracy']+".\n"



#predicted_os="There is {} ".format("hello")


with open("osinfo.txt",'w') as f:
    f.write(host_is_up+port_open+method_scan+predicted_os+prediction_per)
    now=datetime.now();
    f.write("\nTimestamp:"+now.strftime("%Y-%m-%d_%H:%M:%S IST"))

print("\nCompleted....")
