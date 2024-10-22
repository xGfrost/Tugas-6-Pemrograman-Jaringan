import time

def evaluate_grade(nilai):
    if nilai >= 88:
        return "Kriteria A"
    elif nilai >= 77:
        return "Kriteria B"
    elif nilai >= 60:
        return "Kriteria C"
    elif nilai >= 45:
        return "Kriteria D"
    else:
        return "Kriteria E"

# Simulate the 5 processes with specific delays
def process_with_delays():
    grades = [90, 80, 65, 50, 30]  # Example values for testing
    
    # Proses 1 (Delay 2 seconds)
    print("Proses 1 - Nilai:", grades[0], "Hasil:", evaluate_grade(grades[0]))
    time.sleep(2)
    
    # Proses 2 (Delay 3 seconds)
    print("Proses 2 - Nilai:", grades[1], "Hasil:", evaluate_grade(grades[1]))
    time.sleep(3)
    
    # Proses 3 (Delay 4 seconds)
    print("Proses 3 - Nilai:", grades[2], "Hasil:", evaluate_grade(grades[2]))
    time.sleep(4)
    
    # Proses 4 (Delay 5 seconds)
    print("Proses 4 - Nilai:", grades[3], "Hasil:", evaluate_grade(grades[3]))
    time.sleep(5)
    
    # Proses 5 (Delay 6 seconds)
    print("Proses 5 - Nilai:", grades[4], "Hasil:", evaluate_grade(grades[4]))
    time.sleep(6)

# Run the process
process_with_delays()
