import pyshark
# import sys
# print(sys.stdout.encoding)

cap = pyshark.LiveCapture(interface='Wi-Fi')
cap.sniff(timeout=10)
print(cap[0])
