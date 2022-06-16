import pyqrcode
import time
from pyzbar.pyzbar import decode
from PIL import Image

if __name__ == "__main__":

    while 1:
        print("What do you want to do? \n1 - Generate QR Code\n2 - Scan QR Code")
        sa = int(input("Enter your choice: "))

        if sa == 1:
            sen = input("Enter text or URL address: ")
            qr = pyqrcode.create(sen)
            file = input("Under what name you want to save your QR code?: ")
            qr.png(f'{file}.png', scale=8)
            time.sleep(2)
            print("Successfully generated!")

        elif sa == 2:
            say = input("Which file do you want to scan?: ")
            a = decode(Image.open(f"{say}.png"))
            print("Scanning...")
            time.sleep(2)
            print(f"\n Text Scanned: {a[0][0]}")

        else:
            print("Warning! Wrong number! Please enter a valid number!")

        command = input("Do you want to continue? - [yes/no]: ".lower())
        if command == "yes":
            continue
        else:
            exit()

