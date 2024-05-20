import qrcode
import os
from PIL import Image

def generate_qr_code(url, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_path)

    img.show()

SAVED_DIRECTORY = "./inoue/images"

if __name__ == "__main__":
    url = input("QRコードを生成するURLを入力してください: ")
    file_name = input("保存するファイル名を入力してください（例: qr_code.png）: ")

    if not os.path.exists(SAVED_DIRECTORY):
        os.makedirs(SAVED_DIRECTORY)

    file_path = os.path.join(SAVED_DIRECTORY, file_name)

    generate_qr_code(url, file_path)
    print(f"QRコードを{file_path}に保存しました。")