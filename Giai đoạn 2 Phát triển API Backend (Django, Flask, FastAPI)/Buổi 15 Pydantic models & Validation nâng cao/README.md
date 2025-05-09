# Buổi 15 Pydantic models & Validation nâng cao
## 1. Constrained Types & Field Constraints
- Pydantic cung cấp sẵn các kiểu có ràng buộc:
``` Python
from pydantic import BaseModel, conint, constr, confloat, EmailStr, HttpUrl

class Item(BaseModel):
    # Integer >= 0 và <= 100
    quantity: conint(ge=0, le=100)
    # Chuỗi với độ dài 3–50 ký tự
    name: constr(min_length=3, max_length=50)
    # Số thực > 0
    price: confloat(gt=0)
    # Email hợp lệ
    owner_email: EmailStr
    # URL hợp lệ
    image_url: HttpUrl
```

- `conint(ge=…, le=…), confloat(gt=…, lt=…)`
- `constr(min_length=…, regex=…)`

## 2. Nested Models & Tái sử dụng Schema
Bạn có thể lồng BaseModel trong nhau:
``` Python
from typing import List

class Address(BaseModel):
    street: str
    city: str
    zip_code: constr(regex=r'^\d{5}$')

class User(BaseModel):
    username: str
    email: EmailStr
    address: Address
    tags: List[str] = []      # mặc định danh sách rỗng
```
- Truyền JSON dạng:
``` json
{
  "username": "alice",
  "email": "alice@example.com",
  "address": {
    "street": "123 Main St",
    "city": "Hanoi",
    "zip_code": "10000"
  },
  "tags": ["admin","editor"]
}
```
## 3. Custom Validators
Dùng decorator `@validator` để kiểm tra hoặc biến đổi giá trị:
``` Python
from pydantic import validator

class User(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_no_spaces(cls, v):
        if ' ' in v:
            raise ValueError('username không được chứa khoảng trắng')
        return v

    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('password phải có ít nhất 8 ký tự')
        return v
```
- `@validator('field1','field2', pre=True)` để xử lý trước validate type
- `each_item=True` cho list/tuple

## 4. Config Options
Bạn có thể điều chỉnh hành vi qua `class Config` bên trong model:
``` Python
class User(BaseModel):
    user_name: str
    full_name: str

    class Config:
        # Cho phép alias khác tên field
        allow_population_by_field_name = True
        # Khi serialize, dùng alias
        alias_generator = lambda s: s.upper()
        # Cho phép dùng ORM object (SQLAlchemy model)
        orm_mode = True
        # Tùy chỉnh cách JSON encode (ví dụ datetime)
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d')
        }
```
- `orm_mode = True`: hỗ trợ trả model từ ORM
- `alias_generator` hoặc `fields = {...}`: đặt tên JSON khác Python attr

## 5. Ví dụ Hoàn Chỉnh
``` Python
from pydantic import BaseModel, conint, EmailStr, validator
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: constr(regex=r'^\d{5}$')

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: conint(ge=18, le=99)
    address: Address
    tags: List[str] = []
    joined_at: datetime

    @validator('username')
    def no_spaces(cls, v):
        if ' ' in v:
            raise ValueError('username không chứa khoảng trắng')
        return v.lower()

    @validator('tags', each_item=True)
    def tags_lowercase(cls, v):
        return v.lower()

    class Config:
        orm_mode = True
        json_encoders = { datetime: lambda v: v.isoformat() }
```
