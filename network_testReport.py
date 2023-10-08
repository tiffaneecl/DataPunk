##Problem:
##My network speeds are intermittment on both my 2.4 and 5.0
##channels. Because it is not at the same time, I need to
##draw down on when and where my current service is being
##utilized.
##
##I don't currently have any data points that would be helpful
##to the ISP helpdesk in solving this problem.' So we're going
##to mine some using python.
##
##Well...PowerShell and Python.
##
##Couple Topics to have in mind:
##
### OSI Layer Model -
##What is the OSL Model. The Open Systems Interconnection (OSI) model
##describes seven layers that computer systems yse to communicate over
##a network. It was the first standard model fro network commmunications,
##adopted by all major computer and telecommuncation companies in the early
##1980s.
##
##Source: https://www.imperva.com
##
###ICMP
##The Internet Control Message Protocol (ICMP) is a protocol that devices
##within a network use to communicate problems with data transmission.
##
##In this ICMP definitionm one of the primary ways in which ICMP is used
##is to determine if  data is getting to its destination at the right
##time.
##
##AKA: PING
##
##Source: https://www.fortinet.com
##
### SLA
##A service-level agreement (SLA) sets the expectations between the service
##provider and the customer and descibes the products or services to be
##delivered, the single point of contact for end-user problems,
##and the metrics by which the effectiveness of the process is
##monitored and approved.

import speedtest
import time
import datetime

speedTest = speedtest.Speedtest(secure=True)
#option = int(input('''What speed do you want to test: 1 - DL 2 - UL 3 - ICMP'''))

def translateSpeed(inSpeedBits):
        returnSpeed = ''
        if inSpeedBits < 1000:
                returnSpeed = str(round(inSpeedBits, 3))+" bps"
        elif inSpeedBits < 1000000:
                returnSpeed = str(round(inSpeedBits/1000, 3))+" Kbps"
        elif inSpeedBits < 1000000000:
                returnSpeed = str(round(inSpeedBits/1000000, 3))+" Mbps"
        else:
                returnSpeed = str(round(inSpeedBits/1000000000, 3))+" Gbps"
        return returnSpeed

runMe = True
runCount = 0

print("{0} {1} - {2} - {3} {4}".format('Run Count','Download','Upload','PING','Record Time'))
while runMe == True:
        time.sleep(45)
        DL = translateSpeed(speedTest.download())
        UL = translateSpeed(speedTest.upload())
        #print(speedTest.get_best_server())^%
        speedTest.get_servers()
        PING = str(speedTest.results.ping)

        print("{0} {1} - {2} - {3} {4}".format(str(runCount),DL,UL,PING,str(datetime.datetime.now())))
        runCount += 1

        if runCount >= 1000:
                runMe = False




        
