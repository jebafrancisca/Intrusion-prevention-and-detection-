import matplotlib.pyplot as plt
import os
from collections import deque, defaultdict
from scapy.all import sniff, IP
import time
import tkinter as tk
from threading import Thread

request_history = deque(maxlen=20)
ip_count = defaultdict(int)
blocked_ips = set()
start_time = time.time()

REQUEST_LIMIT = 5
TIME_WINDOW = 10
LOG_FILE = "log.txt"
running = False

root = tk.Tk()
root.title("IDS/IPS Monitor")
root.geometry("700x450")

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

def log(msg):
    text_area.insert(tk.END, msg + "\n")
    text_area.see(tk.END)
    with open(LOG_FILE, "a",encoding="utf-8") as f: 
        f.write(msg + "\n")

def block_ip_real(ip):
    os.system(f'netsh advfirewall firewall add rule name="Block_{ip}" dir=in action=block remoteip={ip}')

def process_packet(packet):
    global start_time

    if not running:
        return

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        request_history.append(sum(ip_count.values()))

        if src_ip in blocked_ips:
            log(f"🚫 Blocked packet from {src_ip}")
            return

        ip_count[src_ip] += 1

        if time.time() - start_time > TIME_WINDOW:
            ip_count.clear()
            start_time = time.time()

        if ip_count[src_ip] > REQUEST_LIMIT:
            log(f"\n⚠️ Intrusion Detected from IP: {src_ip}")
            log("🚫 Blocking IP...\n")
            blocked_ips.add(src_ip)
            block_ip_real(src_ip)

def sniff_packets():
    sniff(prn=process_packet, store=False)

def start_monitoring():
    global running
    running = True
    log("▶️ Monitoring Started...\n")

def stop_monitoring():
    global running
    running = False
    log("⏹️ Monitoring Stopped...\n")

def clear_logs():
    text_area.delete(1.0, tk.END)
    open(LOG_FILE, "w").close()
    log("🧹 Logs Cleared\n")

def show_graph():
    plt.plot(list(request_history))
    plt.title("Network Traffic")
    plt.xlabel("Time")
    plt.ylabel("Requests")
    plt.show()

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Start", command=start_monitoring, bg="green", fg="white").grid(row=0, column=0, padx=10)
tk.Button(frame, text="Stop", command=stop_monitoring, bg="red", fg="white").grid(row=0, column=1, padx=10)
tk.Button(frame, text="Clear Logs", command=clear_logs).grid(row=0, column=2, padx=10)
tk.Button(frame, text="Show Graph", command=show_graph).grid(row=0, column=3, padx=10)

Thread(target=sniff_packets, daemon=True).start()

log("🚀 IDS/IPS Ready. Click Start.\n")

root.mainloop()