import qrcode

# Đường dẫn trang web của bạn (Sau khi bạn đã upload file html lên mạng)
# Nếu chưa có, bạn có thể thử với một link ảnh online hoặc link video kỷ niệm
url = "https://your-valentines-link.com" 

# Cấu hình QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Tạo ảnh QR với màu sắc lãng mạn
img = qr.make_image(fill_color="#ff4d4d", back_color="white")

# Lưu file
img.save("valentine_qr.png")
print("Đã tạo xong mã QR 'valentine_qr.png'. Hãy gửi nó cho người ấy nhé!")