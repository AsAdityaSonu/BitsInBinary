import qrcode

def generate_qr(data, filename='qr_code.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    user_input = input("Enter text or URL to generate QR Code: ")
    filename = input("Enter file name to save (with .png): ").strip()
    if not filename:
        filename = "qr_code.png"
    generate_qr(user_input, filename)