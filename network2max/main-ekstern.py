# Sends web traffic packet information from all wifi to localhost on port 8888.
import argparse
import pyshark
from pythonosc import udp_client

# Legg til IPer til andre nettsteder (f.eks facebook, skolen din etc.)
ekstern_ip = "192.168.86.39"
prev_pkt_len = ""

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--osc_ip", default="127.0.0.1")
    parser.add_argument("--ekstern_ip", default=ekstern_ip)
    parser.add_argument("--osc_port", type=int, default=8888)
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.osc_ip, args.osc_port)

    print(f"Sending OSC packets to {args.osc_ip} on port {args.osc_port}.")
    print(f"Press Ctrl+C to stop.")

    # with geoip2.database.Reader('/path/to/maxmind-database.mmdb') as reader:
    # bpf_filter="ip and host "+ekstern_ip+""
    cap = pyshark.LiveCapture(interface="Wi-Fi")

    for pkt in cap:
        # Prevent identical connections from happening twice
        if (prev_pkt_len != pkt.length):

            if "IP" in pkt:
                protocol = pkt.highest_layer
                source = pkt.ip.src
                dest = pkt.ip.dst
                prev_pkt_len = pkt.length

                try:
                    # print("[Protocol:] "+protocol+" [Source IP:] "+source +
                    #     " [Destination IP:] "+dest+" [Size:] "+pkt.length)

                    # To OSC
                    if pkt.highest_layer == "TLS":
                        client.send_message("/protocol", 0)
                    elif pkt.highest_layer == "TCP":
                        client.send_message("/protocol", 1)
                    elif pkt.highest_layer == "DNS":
                        client.send_message("/protocol", 2)
                    elif pkt.highest_layer == "HTML":
                        client.send_message("/protocol", 3)
                    else:
                        client.send_message("/protocol", 4)

                    if dest == args.ekstern_ip:
                        print("[Protocol:] "+protocol+" [Source IP:] "+source +
                        " [Destination IP:] "+dest+" [Size:] "+pkt.length)
                        #dsp = reader.city(pkt.ip.src)
                        client.send_message("/packet_len", int(pkt.length))
                        client.send_message('/src_ip', source)
                        client.send_message("/dst_ip", dest)

                except:
                    print("Error with sending OSC..")
