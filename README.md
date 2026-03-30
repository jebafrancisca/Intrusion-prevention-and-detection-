# 🚀 Intrusion Detection and Prevention System (IDPS)

## 📌 Overview

This project is a **real-time Intrusion Detection and Prevention System (IDPS)** built using Python.
It monitors network traffic, detects suspicious activity based on request frequency, and automatically blocks malicious IP addresses.

The system also provides a **Graphical User Interface (GUI)** for monitoring logs and controlling the detection process.

---

## 🎯 Features

* 🔍 Real-time packet monitoring using Scapy
* ⚠️ Detects suspicious traffic (e.g., high request rate / flooding)
* 🚫 Automatically blocks malicious IP addresses
* 🖥️ User-friendly GUI using Tkinter
* 📊 Traffic visualization using Matplotlib
* 🧾 Logging system for detected intrusions

---

## 🛠️ Technologies Used

* Python
* Scapy (for packet sniffing)
* Tkinter (for GUI)
* Matplotlib (for visualization)

---

## ⚙️ How It Works

1. The system continuously monitors incoming network packets.
2. It tracks the number of requests from each IP address.
3. If an IP exceeds a defined threshold within a time window:

   * It is flagged as suspicious
   * The IP is blocked using firewall rules
4. All activities are logged and displayed in the GUI.

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/intrusion-detection-system.git
cd intrusion-detection-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application using:

```bash
python main.py
```

### GUI Controls:

* ▶️ **Start** → Begin monitoring network traffic
* ⏹️ **Stop** → Stop monitoring
* 🧹 **Clear Logs** → Clear log file and UI
* 📊 **Show Graph** → Display traffic visualization

---

## ⚠️ Important Notes

* This project uses **Scapy**, which may require administrator/root privileges.
* The IP blocking feature uses:

  ```
  netsh advfirewall
  ```

  👉 This works only on **Windows systems**.

---

## 📂 Project Structure

```
intrusion-detection-system/
│
├── main.py
├── requirements.txt
├── log.txt
└── README.md
```

---

## 📊 Output

* Real-time logs displayed in GUI
* Log file (`log.txt`) stores all intrusion events
* Graph showing network traffic patterns

---

## 🚀 Future Improvements

* 🌐 Web-based dashboard
* 🤖 Machine Learning-based attack detection
* 📡 Support for multiple network interfaces
* 🔐 Cross-platform firewall integration

---

## 👨‍💻 Author

Developed as a cybersecurity project using Python.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
