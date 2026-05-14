# import threading

# def even():
#     for i in range(2, 21, 2):
#         print("Even:", i)

# def odd():
#     for i in range(1, 21, 2):
#         print("Odd:", i)

# t1 = threading.Thread(target=even)
# t2 = threading.Thread(target=odd)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Done")

import threading
import time

def download(file):
    print(f"Downloading {file}...")
    time.sleep(2)
    print(f"{file} downloaded.")

files = ["file1.jpg", "file2.mp4", "file3.pdf"]

threads = []

for file in files:
    t = threading.Thread(target=download, args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads completed.")