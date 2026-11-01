import qrcode

url = input("Enter the URL to generate QR code: ").strip()

if not url:
    print("Please enter a valid URL.")
else:
    file_path = "qrcode.png"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    print("QR Code successfully generated!")
    print(f"Saved as: {file_path}")