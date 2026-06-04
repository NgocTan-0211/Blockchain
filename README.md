# Smart Anti Theft Blockchain

## Giới thiệu

Smart Anti Theft Blockchain là hệ thống chống trộm thông minh ứng dụng Trí tuệ nhân tạo (AI) và công nghệ Blockchain nhằm giám sát, phát hiện và lưu trữ các sự kiện xâm nhập một cách an toàn, minh bạch.

Hệ thống sử dụng mô hình YOLOv8 để phát hiện người theo thời gian thực từ webcam. Khi phát hiện đối tượng, hệ thống sẽ tự động chụp ảnh, tạo mã băm SHA-256, lưu dữ liệu lên Blockchain thông qua Smart Contract Solidity và đồng thời lưu thông tin vào cơ sở dữ liệu MySQL để phục vụ quản lý và tra cứu.

---

## Mục tiêu

* Phát hiện người xâm nhập bằng AI.
* Chụp ảnh và lưu bằng chứng tự động.
* Tạo mã băm SHA-256 cho ảnh.
* Lưu mã băm lên Blockchain nhằm đảm bảo tính toàn vẹn dữ liệu.
* Quản lý sự kiện trên Web Dashboard.
* Hỗ trợ truy xuất và xác thực dữ liệu.

---

## Công nghệ sử dụng

### Trí tuệ nhân tạo (AI)

* YOLOv8
* OpenCV
* Python

### Blockchain

* Solidity
* Remix IDE
* Ganache
* MetaMask
* Web3.py

### Backend

* Flask
* Python

### Database

* MySQL

### Frontend

* HTML
* CSS
* Bootstrap

---

## Cấu trúc thư mục

```text
SmartAntiTheftBlockchain/
│
├── ai/
│   ├── detect.py
│   └── hash_utils.py
│
├── backend/
│   ├── app.py
│   ├── blockchain.py
│   └── database.py
│
├── blockchain/
│   ├── AntiTheft.sol
│   └── abi.json
│
├── templates/
│   ├── index.html
│   └── history.html
│
├── uploads/
│
└── requirements.txt
```

---

## Chức năng chính

### 1. Phát hiện người bằng AI

* Sử dụng YOLOv8 nhận diện người từ webcam.
* Xử lý theo thời gian thực.
* Tự động chụp ảnh khi phát hiện đối tượng.

### 2. Tạo mã băm SHA-256

* Sinh mã hash duy nhất cho mỗi ảnh.
* Phục vụ xác thực dữ liệu.

### 3. Lưu dữ liệu Blockchain

* Smart Contract Solidity lưu hash ảnh.
* Đảm bảo dữ liệu không bị chỉnh sửa.

### 4. Lưu trữ cơ sở dữ liệu

* Quản lý lịch sử sự kiện.
* Lưu đường dẫn ảnh.
* Lưu Transaction Hash.

### 5. Dashboard quản trị

* Hiển thị lịch sử cảnh báo.
* Xem ảnh đã lưu.
* Tra cứu dữ liệu Blockchain.

---

## Yêu cầu hệ thống

### Phần mềm

* Python 3.10
* Anaconda
* Visual Studio Code
* MySQL Server
* Ganache
* MetaMask

### Thư viện Python

```bash
pip install flask
pip install opencv-python
pip install ultralytics
pip install web3
pip install mysql-connector-python
pip install pillow
pip install numpy
```

---

## Cài đặt cơ sở dữ liệu

```sql
CREATE DATABASE antitheft;

USE antitheft;

CREATE TABLE events(
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_path TEXT,
    hash_value TEXT,
    tx_hash TEXT,
    timestamp DATETIME
);
```

---

## Triển khai Smart Contract

1. Mở Remix IDE.
2. Tạo file AntiTheft.sol.
3. Compile bằng Solidity 0.8.20.
4. Deploy bằng MetaMask.
5. Kết nối mạng Ganache.
6. Lưu Contract Address.
7. Copy ABI vào file abi.json.

---

## Chạy hệ thống

### Bước 1: Kích hoạt môi trường

```bash
conda activate antitheft
```

### Bước 2: Chạy Flask

```bash
python backend/app.py
```

### Bước 3: Chạy AI Detection

```bash
python ai/detect.py
```

### Bước 4: Truy cập Dashboard

```text
http://127.0.0.1:5000
```

---

## Luồng hoạt động hệ thống

```text
Webcam
   ↓
YOLOv8
   ↓
Phát hiện người
   ↓
Chụp ảnh
   ↓
SHA256
   ↓
Blockchain
   ↓
MySQL
   ↓
Dashboard
```

---

## Kết quả đạt được

* Phát hiện người theo thời gian thực.
* Tự động lưu ảnh.
* Tạo mã băm SHA-256.
* Lưu dữ liệu lên Blockchain.
* Lưu lịch sử sự kiện trong MySQL.
* Quản lý dữ liệu qua giao diện Web.

---

## Hướng phát triển

* Tích hợp ESP32-CAM.
* Cảnh báo Telegram.
* Cảnh báo Email.
* Xác thực dữ liệu Blockchain trên Dashboard.
* Nhận diện khuôn mặt người lạ.
* Hỗ trợ IP Camera.
* Triển khai Cloud Server.

---

## Tác giả

Họ và tên: Lù Ngọc Tân

Mã sinh viên: 1671020281

Lớp: CNTT 16-01

Đề tài: Hệ thống chống trộm thông minh sử dụng AI và Blockchain

Năm thực hiện: 2026
