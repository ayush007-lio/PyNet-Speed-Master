<div align="center">

  # 🚀 Network Speed Master
  
  **A lightning-fast, dual-mode Internet Speed Tester built with Python.**

  ![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)
  ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
  ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)

  <p align="center">
    <img src="assets/preview.png" alt="App Screenshot" width="600"/>
  </p>

  [Report Bug](https://github.com/issues) • [Request Feature](https://github.com/issues)
</div>

---

## 📖 About
**Network Speed Master** is a lightweight utility designed to measure your internet connection's performance accurately. Whether you prefer a raw **Command Line Interface (CLI)** for server environments or a modern **Dark-Mode GUI** for your desktop, this tool has you covered.

## ✨ Key Features

* **⚡ Dual Interface:** Choose between a threaded GUI or a lightweight CLI.
* **📊 Comprehensive Metrics:** Measures Download, Upload, and Ping (Latency).
* **🎨 Modern UI:** Clean, dark-themed interface built with Tkinter.
* **🔄 Multi-threaded:** Prevents "Application Not Responding" errors during testing.
* **💾 Lightweight:** Minimal dependencies, utilizing `speedtest-cli`.

---

## 🛠️ Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/NetworkSpeedTester.git](https://github.com/YOUR_USERNAME/NetworkSpeedTester.git)
    cd NetworkSpeedTester
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

### 🖥️ GUI Version (Desktop)
Launch the graphical interface for a visual experience:
```bash
python gui_speed_test.py

📟 CLI Version (Terminal)
Run the test directly in your terminal (perfect for remote servers):

python speed_test.py

📂 Project Structure
Plaintext

NetworkSpeedTester/
├── assets/              # Screenshots and images
├── gui_speed_test.py    # Main GUI Application source code
├── speed_test.py        # CLI Application source code
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
