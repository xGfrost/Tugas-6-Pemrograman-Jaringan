import socket
import platform
import threading
import time

# Fungsi untuk thread countdown
def countdown(name, start_value):
    print(f"{name} mulai countdown dari {start_value}")
    for i in range(start_value, 0, -1):
        print(f"{name}: {i}")
        time.sleep(1)  # Delay 1 detik
    print(f"{name} selesai!")

def get_service_by_port():
    try:
        port = int(input("Masukkan port protokol: "))
        service_name = socket.getservbyport(port)
        print(f"Port: {port} => service name: {service_name}")
    except OSError:
        print(f"Port: {port} tidak memiliki service name yang terdaftar.")
    except ValueError:
        print("Input harus berupa angka.")

def get_ip_address():
    try:
        website = input("Masukkan alamat web: ")
        ip_address = socket.gethostbyname(website)
        local_ip = socket.gethostbyname(socket.gethostname())
        computer_name = platform.node()
        print(f"Anda mengakses {website} dengan alamat IP {ip_address} dari komputer {computer_name} dengan alamat IP {local_ip}")
    except socket.gaierror:
        print("Alamat web tidak valid.")

# Fungsi untuk memulai thread countdown
def start_threads():
    threads = []
    
    # Membuat 5 thread dengan countdown masing-masing
    threads.append(threading.Thread(target=countdown, args=("Thread 1", 3)))
    threads.append(threading.Thread(target=countdown, args=("Thread 2", 6)))
    threads.append(threading.Thread(target=countdown, args=("Thread 3", 9)))
    threads.append(threading.Thread(target=countdown, args=("Thread 4", 12)))
    threads.append(threading.Thread(target=countdown, args=("Thread 5", 15)))

    # Memulai semua thread
    for thread in threads:
        thread.start()

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

def main():
    while True:
        print("\nMENU PILIHAN:")
        print("1. MENGETAHUI SERVICE DAN PROTOKOL PADA JARINGAN")
        print("2. MENGETAHUI ALAMAT IP DARI SEBUAH WEBSITE")
        print("3. MENJALANKAN THREAD COUNTDOWN")
        
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            get_service_by_port()
        elif choice == '2':
            get_ip_address()
        elif choice == '3':
            start_threads()
        else:
            print("Pilihan tidak valid.")

        repeat = input("ANDA INGIN MENGULANG (Y/T)? ").upper()
        if repeat != 'Y':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()
