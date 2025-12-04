import speedtest

def main():
    print("Network Speed Test (CLI Version)")
    st = speedtest.Speedtest()
    st.get_best_server()
    print("Testing Download Speed...")
    download_speed = st.download() / 1_000_000
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print("Testing Upload Speed...")
    upload_speed = st.upload() / 1_000_000
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print("Testing Ping...")
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    main()
