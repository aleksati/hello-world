import pyshark

cap = pyshark.LiveCapture(interface='eth0', disable_protocol=False)
cap.sniff(timeout=10)
print(cap)
