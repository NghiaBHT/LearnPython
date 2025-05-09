### Bài 1: Product Model
- Fields:
    - `id`: int
    - `name`: constr(min_length=3)
    - `price`: confloat(gt=0)
    - `tags`: List[constr(min_length=2)] với mỗi tag không có ký tự số
- Validator:
    - `name` không được chứa ký tự đặc biệt (regex)
    - `tags`: mỗi mục lowercase
### Bài 2: Order Model
- Nested `User` và `List[Product]`
- Field `total`: float tính tự động qua `@validator` (sum giá sản phẩm)
- Field `status`: constr(regex='^(pending|shipped|delivered)$')

