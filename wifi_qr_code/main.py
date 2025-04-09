import qrcode

ssid=input("Enter Your Wifi Name (SSID): ")
password=input("Ener Your Wifi Password: ")
encryption= "WPA" #or change it into WEP or "" if nbeeded

data=f"WIFI:T:{encryption};S:{ssid};P:{password};;"
img= qrcode.make(data)
img.save("wifi_qrcode.png")

print("✅ QR code saved as 'wifi_qr.png'. Scan it to connect!")