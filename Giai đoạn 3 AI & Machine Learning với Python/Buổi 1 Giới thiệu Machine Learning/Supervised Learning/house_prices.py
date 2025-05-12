'''
Một công ty bất động sản muốn xây hệ thống ước tính giá bán dựa trên một số đặc trưng của bất động sản:
Diện tích (area), số phòng ngủ (bedrooms), số phòng tắm (bathrooms), vị trí (location), tuổi nhà (age), v.v.
Đầu ra: giá bán (liên tục, ví dụ tính theo triệu đồng).
Mục tiêu:
Xây mô hình Regression (hồi quy) để dự đoán giá dựa trên dữ liệu lịch sử.
Đánh giá mô hình bằng RMSE và R^2

Xây dựng pipeline
1. Load dữ liệu với pandas
2. Tiền xử lý
    - Xử lý missing (nếu có)
    - One-Hot Encoding cho location
    - Scale (StandardScaler) cho các biến số
3. Chia train/test (70/30)
4. Huấn luyện model: Linear Regression & Random Forest Regressor
5. Đánh giá: RMSE & R^2 
6. So sánh kết quả hai model
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load dữ liệu
df = pd.read_csv("house_prices.csv")

# 2. Tiền xử lý
# 2.1 Xử lý missing bằng cách gán lại (không dùng inplace trên slice)
for col in ["area","bedrooms","bathrooms","age","price"]:
    df[col] = df[col].fillna(df[col].median())

# 2.2 One-Hot Encoding cho location
df = pd.get_dummies(df, columns=["location"], drop_first=True)

# 2.3 Tách X, y
X = df.drop("price", axis=1)
y = df["price"]

# 3. Train/Test split đảm bảo đủ mẫu test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Số mẫu train: {len(y_train)}, test: {len(y_test)}")

# 4. Pipeline scale + model
pipelines = {
    "Linear": Pipeline([
        ("scale", StandardScaler()),
        ("model", LinearRegression())
    ]),
    "RandomForest": Pipeline([
        ("scale", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42))
    ])
}

# 5. Huấn luyện & đánh giá
results = {}
for name, pipe in pipelines.items():
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2  = r2_score(y_test, y_pred)
    results[name] = {"RMSE": rmse, "R2": r2}

# In kết quả
for name, metrics in results.items():
    print(f"{name:15s} → RMSE: {metrics['RMSE']:.2f}, R2: {metrics['R2']:.3f}")
