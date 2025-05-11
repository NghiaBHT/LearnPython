# Buổi 17: Quan hệ giữa các bảng (One-to-Many & Many-to-Many) trong SQLAlchemy
### 1. One-to-Many: User ↔ Post
#### 1.1. Định nghĩa models
```python
# app/db/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id       = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email    = Column(String, unique=True, index=True)

    # One user có nhiều posts
    posts    = relationship("Post", back_populates="owner", cascade="all, delete")


class Post(Base):
    __tablename__ = "posts"

    id        = Column(Integer, primary_key=True, index=True)
    title     = Column(String, index=True)
    content   = Column(String)
    owner_id  = Column(Integer, ForeignKey("users.id"))

    # Post tham chiếu ngược đến User
    owner     = relationship("User", back_populates="posts")
```
- `ForeignKey("users.id")` liên kết `Post.owner_id` với `User.id`.
- `relationship(..., back_populates=...)` tạo thuộc tính để duyệt quan hệ.

### 2. Many-to-Many: Post ↔ Tag
#### 2.1. Bảng phụ (Association Table)
```python
# app/db/models.py (tiếp)
from sqlalchemy import Table

post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)

class Tag(Base):
    __tablename__ = "tags"

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    posts = relationship("Post", secondary=post_tag, back_populates="tags")

# Cập nhật Post model:
class Post(Base):
    # ...
    tags = relationship("Tag", secondary=post_tag, back_populates="posts")
```
- Bảng `post_tag` lưu cặp `(post_id, tag_id)`.
- Sử dụng `secondary=post_tag` để chỉ SQLAlchemy join.