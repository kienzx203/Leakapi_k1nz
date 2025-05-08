import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from pathlib import Path

url = "https://wordlists-cdn.assetnote.io/data/automated/"
output_directory = "C:\\Users\\dungn\\wordlists\\test"

# Tạo thư mục đầu ra nếu nó không tồn tại
os.makedirs(output_directory, exist_ok=True)

# Gửi yêu cầu GET đến URL
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công hay không (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích cú pháp HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Lấy tất cả các thẻ <a> chứa liên kết
    links = soup.find_all('a')
    # print(links)
    # Lặp qua từng thẻ <a> và tải về các file .txt
    for link in links:
        file_url = urljoin(url, link.get('href'))
        file_name = os.path.join(output_directory, os.path.basename(file_url))

        # Kiểm tra xem liên kết có phải là file .txt hay không
        if Path(file_name).suffix.lower() == '.txt':
            # Tải file và lưu vào thư mục đầu ra
            with open(file_name, 'wb') as file:
                file.write(requests.get(file_url).content)

            print(f"Downloaded: {file_name}")
else:
    print(f"Failed to retrieve content. Status Code: {response.status_code}")
