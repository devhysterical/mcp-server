# MCP Server

MCP Server là một máy chủ triển khai giao thức Model Context Protocol (MCP), cho phép các mô hình ngôn ngữ lớn (LLMs) tương tác với các công cụ và dịch vụ bên ngoài một cách chuẩn hóa.

## Tính năng

- Hỗ trợ nhiều công cụ khác nhau (calculator, weather, search)
- API RESTful với FastAPI
- Xác thực dữ liệu với Pydantic
- Xử lý bất đồng bộ hiệu quả
- Tài liệu API tự động với Swagger UI

## Yêu cầu hệ thống

- Python 3.8+
- pip (Python package manager)

## Cài đặt

1. Clone repository:

```bash
git clone <repository-url>
cd mcp-server
```

2. Tạo và kích hoạt môi trường ảo:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## Chạy server

```bash
python main.py
```

Server sẽ chạy tại địa chỉ: http://localhost:8000

## API Endpoints

### 1. Root Endpoint

- **URL**: `/`
- **Method**: GET
- **Description**: Trả về thông tin về server và danh sách các công cụ được hỗ trợ

### 2. Execute Tool

- **URL**: `/execute`
- **Method**: POST
- **Description**: Thực thi một công cụ với các tham số được cung cấp
- **Request Body**:

```json
{
  "tool_name": "calculator",
  "parameters": {
    "operation": "add",
    "numbers": [1, 2, 3]
  },
  "context": {}
}
```

## Các công cụ được hỗ trợ

### 1. Calculator

- Thực hiện các phép tính cơ bản
- Tham số:
  - `operation`: "add" hoặc "multiply"
  - `numbers`: mảng các số cần tính

### 2. Weather

- Lấy thông tin thời tiết cho một địa điểm
- Tham số:
  - `location`: tên địa điểm

### 3. Search

- Thực hiện tìm kiếm web
- Tham số:
  - `query`: từ khóa tìm kiếm

## Tài liệu API

Truy cập http://localhost:8000/docs để xem tài liệu API đầy đủ với Swagger UI.

## Phát triển

### Thêm công cụ mới

1. Thêm tên và mô tả công cụ vào `SUPPORTED_TOOLS`
2. Thêm hàm xử lý mới trong `process_tool_request`
3. Tạo hàm xử lý riêng cho công cụ mới

### Chạy tests

```bash
pytest
```

## License

MIT License
