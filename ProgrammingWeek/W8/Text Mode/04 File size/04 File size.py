#Written in Python IDLE 3.14.6
import os

directory = input("Enter directory path: ")

total_size = 0
image_size = 0

print("\nAll files:")

for file in os.listdir(directory):
    path = os.path.join(directory, file)

    if os.path.isfile(path):
        size = os.path.getsize(path)
        total_size += size

        print(file, "-", size, "bytes")

print("\nTotal file size:", total_size, "bytes")

print("\nImage files:")

for file in os.listdir(directory):
    path = os.path.join(directory, file)

    if os.path.isfile(path):
        if file.lower().endswith((".jpg", ".gif", ".png")):
            size = os.path.getsize(path)
            image_size += size

            print(file, "-", size, "bytes")

print("\nTotal image file size:", image_size, "bytes")
