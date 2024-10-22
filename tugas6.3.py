import threading
import time

# Fungsi untuk mencetak bilangan ganjil dari 1 hingga 10
def print_odd_numbers():
    for i in range(1, 11, 2):  # Mencetak bilangan ganjil
        print(f"Thread 1 - Odd: {i}")
        time.sleep(1)  # Delay 1 detik

# Fungsi untuk mencetak bilangan genap dari 1 hingga 10
def print_even_numbers():
    for i in range(2, 11, 2):  # Mencetak bilangan genap
        print(f"Thread 2 - Even: {i}")
        time.sleep(1)  # Delay 1 detik

# Membuat thread
thread1 = threading.Thread(target=print_odd_numbers)
thread2 = threading.Thread(target=print_even_numbers)

# Menjalankan thread
thread1.start()
thread2.start()

# Menunggu kedua thread selesai
thread1.join()
thread2.join()
