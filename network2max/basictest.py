import pyshark

cap = pyshark.LiveCapture(interface="Wi-Fi")
cap.sniff(timeout=5)

for pkt in cap:
    print(pkt)
