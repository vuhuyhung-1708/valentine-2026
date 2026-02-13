import qrcode

# Link GitHub Pages lấy từ ảnh của bạn
url = "https://vuhuyhung-1708.github.io/valentine-2026/" 

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Tạo ảnh QR với màu đỏ cho đúng tinh thần Valentine
img = qr.make_image(fill_color="#e63946", back_color="white")

# Lưu file ảnh
img.save("valentine_qr_final.png")
print("Đã tạo xong mã QR! Hãy quét thử để tận hưởng thành quả nhé.")