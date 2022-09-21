# Importing via ((((pip install PyQRCode))))
import pyqrcode
import pyfiglet

def qrcodegenerator():
    data = input("Enter the text or link to generate QR code: ")

# Using pyqrcode.create() to create a qr code of the input data
    qr = pyqrcode.create(data)

# Using .svg method to save the qr code as SVG file of provided name & scale
    qr.svg('qr_code.svg', scale = 8)

# Message for code printed 
    print("Your QR Code has been saved in your system as ")
    print(pyfiglet.figlet_format("qr_code.svg", font="digital"))

qrcodegenerator()