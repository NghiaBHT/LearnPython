# Buổi 22: Kết nối RabbitMQ với FastAPI 🐰📨
### 1. Khởi chạy RabbitMQ bằng Docker
```bash
docker run -d --name rabbitmq \
  -p 5672:5672 -p 15672:15672 \
  rabbitmq:3-management
```
- 5672: port AMQP

- 15672: port giao diện quản lý (username/password mặc định `guest/guest`)

- Truy cập giao diện quản lý: http://localhost:15672
### 2. Cài thư viện Python
Trong virtualenv của bạn:
```bash
pip install aio-pika fastapi uvicorn
```
- `aio_pika`: thư viện AMQP bất đồng bộ
- `fastapi`, `uvicorn`: framework và server

### 3. Cấu trúc thư mục gợi ý
```bash
api_project/
├── app/
│   ├── main.py
│   ├── tasks.py            # producer & consumer logic
│   └── db/                 # (nếu có)
├── requirements.txt
└── README.md
```
### 4. Cài đặt producer & consumer
#### 4.1. Tạo module `tasks.py`
```python
# app/tasks.py
import asyncio
import json
from aio_pika import connect, Message, IncomingMessage, ExchangeType

RABBIT_URL = "amqp://guest:guest@localhost/"

async def get_connection():
    return await connect(RABBIT_URL)

# Producer: gửi message vào exchange/queue
async def send_message(queue_name: str, payload: dict):
    connection = await get_connection()
    channel = await connection.channel()
    # Tạo exchange kiểu direct
    exchange = await channel.declare_exchange("fastapi_exchange", ExchangeType.DIRECT)
    message = Message(body=json.dumps(payload).encode())
    # Đảm bảo queue tồn tại và bind với exchange
    queue = await channel.declare_queue(queue_name, durable=True)
    await queue.bind(exchange, routing_key=queue_name)
    # Gửi
    await exchange.publish(message, routing_key=queue_name)
    await connection.close()

# Consumer: lắng nghe queue và xử lý message
async def consume(queue_name: str, handler):
    connection = await get_connection()
    channel = await connection.channel()
    queue = await channel.declare_queue(queue_name, durable=True)
    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                body = message.body.decode()
                data = json.loads(body)
                await handler(data)
```
#### 4.2. Handler ví dụ
```python
# app/tasks.py (cuối file)
async def example_handler(data: dict):
    # Ví dụ: in ra hoặc lưu vào DB
    print("Received message:", data)
```
### 5. Tích hợp với FastAPI
#### 5.1. Gửi message từ endpoint
```python
# app/main.py
from fastapi import FastAPI, BackgroundTasks
from app.tasks import send_message

app = FastAPI()

@app.post("/publish/")
async def publish(item_id: int, background_tasks: BackgroundTasks):
    payload = {"item_id": item_id, "action": "process"}
    # Gửi bất đồng bộ trong background
    background_tasks.add_task(send_message, "task_queue", payload)
    return {"status": "Message queued"}
```
#### 5.2. Khởi chạy consumer riêng
- Tạo file `worker.py` ngoài FastAPI:
```python
# worker.py
import asyncio
from app.tasks import consume, example_handler

async def main():
    print("Starting consumer...")
    await consume("task_queue", example_handler)

if __name__ == "__main__":
    asyncio.run(main())
```
- Chạy worker:
    ```bash
    python worker.py
    ```
Consumer sẽ in payload mỗi khi có message mới.

### 6. Bài tập thực hành
1. Producer/Consumer đơn giản

Endpoint `POST /orders/`: nhận `order_id`, gửi vào queue `"orders"` với payload `{"order_id": ..., "timestamp": ...}`.

Viết `worker.py` lắng nghe queue `"orders"` và in ra “Processing order `<order_id>` at `<timestamp>`”.

2. Xử lý lỗi & retry

Trong handler, giả lập lỗi (raise exception) với 50% xác suất, và nếu thất bại, gửi lại message vào queue `"orders_retry"`.

Tạo consumer cho `"orders_retry"` để thử lại.

3. Persistence & Durability

Cấu hình exchange/queue durable, message persistent.

Thử restart RabbitMQ: message lưu lại trong queue không mất.