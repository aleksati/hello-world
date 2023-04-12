import pyshark
# import sys
# print(sys.stdout.encoding)

cap = pyshark.LiveCapture(interface='wifi')
cap.set_debug()
cap.sniff(timeout=1)
