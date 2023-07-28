import threading
import time

Number = 4
lock = threading.Lock()

# Function to be executed by Thread 1
def Add():
    global Number
    while Number > 1:
        with lock:
            Number += 3
            print("Add ", Number)
        time.sleep(1)

# Function to be executed by Thread 2
def Sub():
    global Number
    while Number < 11:
        with lock:
            Number -= 2
            print("Sub ", Number)
        time.sleep(0.4)

# Create Thread 1
thread1 = threading.Thread(target=Add)

# Create Thread 2
thread2 = threading.Thread(target=Sub)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
