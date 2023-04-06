import aprslib

#PAYLOAD transmitting station callsign
callsign = "draco"

passcode = "hellokitty"

#the device to send the message to
recipient_callsign = "NASA-CALLSIGN"

#example message
message = "Hello Jorge and Juliam"



aprsis_connection = aprslib.IS(callsign, passwd=passcode, host="rotate.aprs.net", port=14580)


aprsis_connection.connect()

'''
TCPIP* indicates that the packet is sent over the 
internet = APRS-IS
rather than via 
RF = radio frequency.
'''
#Send the message
aprsis_connection.sendall(f"{callsign}>APRS,TCPIP*:: {recipient_callsign}:{message}\n")

print(f"Message '{message}' sent to {recipient_callsign}.")


# Disconnect from the APRS-IS server
aprsis_connection.close()
