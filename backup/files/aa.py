import os
import time
import shutil
import bluetooth
import lightblue

while True:
	if os.path.exists("/home/pi/Desktop/receipts/bluetooth.txt"):
	 	f = open('/home/pi/Desktop/receipts/bluetooth.txt')
		lines = f.read()
		target_name = lines.rstrip('\n')
		f.close()
		if not target_name:
			continue
		print target_name
		obex_port = None
		target_address = None
		print "searching for nearby devices..."
		nearby_devices = bluetooth.discover_devices()
		print nearby_devices
		for bdaddr in nearby_devices:
			if target_name == bluetooth.lookup_name(bdaddr):
				target_address = bdaddr
				print "searching for the object push service..."
				print target_address
				# services = lightblue.findservices(addr=target_address, name=target_address, servicetype=None)
				# services = bluetooth.find_service(name=target_name, uuid='0008', address=target_address)
				devices = [ target_address ]
				results = []
                for addr in devices:
                    s = bluetooth._bt.SDPSession()
                    s.connect(addr)
                    matches = []
                    matches = s.browse()
                    if target_name is not None:
                        matches = filter (lambda s: s.get ("name", "") == target_name, \
			                        matches)
                    for m in matches:
                        m["host"] = addr
                    results.extend (matches)
                    print results
				# for service in services:
				# 	if service[2] == "OBEX Object Push" and service[0] == target_address:
				# 	   	obex_port = service[1]
				# 	   	print "OK, service '", service[2], "' is in port", service[1], "!"
				# 	   	break
				# 	elif service[2] == "OPP" and service[0] == target_address:
				# 		obex_port = service[1]
				# 	   	print "OK, service '", service[2], "' is in port", service[1], "!"
				# 	   	break



		# while True:
		# 	if os.path.exists("/home/pi/Desktop/receipts/receipt.jpg"):
		# 	    print "sending a file..."
		# 	    if target_address:
		# 	    	os.system("obexftp --nopath --noconn --uuid none --bluetooth "+target_address+" --channel {} -p /home/pi/Desktop/receipts/receipt.jpg".format(obex_port))
		# 	    	os.remove("/home/pi/Desktop/receipts/receipt.jpg")
		# 	    	os.remove("/home/pi/Desktop/receipts/bluetooth.txt")
		# 	    break
