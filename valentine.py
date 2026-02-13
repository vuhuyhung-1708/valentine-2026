import qrcode
import os

# Link GitHub Pages
url = "https://vuhuyhung-1708.github.io/valentine-2026/" 

# Tạo thư mục images nếu chưa tồn tại
if not os.path.exists("images"):
    os.makedirs("images")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Tạo ảnh QR màu đỏ
img = qr.make_image(fill_color="#e63946", back_color="white")

# Lưu vào thư mục images
img.save("images/valentine_qr_final.png")

print("Đã tạo xong mã QR trong thư mục images!")
