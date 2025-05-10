import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import numpy as np

# بارگذاری داده‌ها
df = pd.read_csv('data/top_coins.csv')

# فیلتر کردن داده‌های معتبر
df = df[['id', 'symbol', 'name', 'current_price', 'price_change_percentage_24h', 'market_cap', 'total_volume']]
df = df.dropna()  # حذف داده‌های خالی

# چاپ مقادیر غیرمجاز (infinity یا بیش از حد بزرگ)
print("Check for infinity or large values:")
print(df[(df > 1e12) | (df < -1e12)])

# جایگزینی مقادیر بیش از حد بزرگ به NaN
max_value = 1e12
df = df.applymap(lambda x: np.nan if isinstance(x, (int, float)) and abs(x) > max_value else x)

# حذف مقادیر NaN
df = df.dropna()

# اضافه کردن ویژگی جدید
df['price_to_volume'] = df['current_price'] / df['total_volume']

# تقسیم داده‌ها به ورودی و خروجی
X = df[['current_price', 'price_change_percentage_24h', 'market_cap', 'total_volume', 'price_to_volume']]
y = df['price_change_percentage_24h']

# مقیاس‌دهی داده‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# تقسیم داده‌ها به مجموعه آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# آموزش مدل
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# پیش‌بینی و ارزیابی مدل
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# ذخیره مدل
joblib.dump(model, 'model/crypto_model.pkl')
joblib.dump(scaler, 'model/scaler.pkl')
