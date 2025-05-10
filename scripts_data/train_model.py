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

# حذف داده‌های با مقدار بی‌نهایت (infinity)
df = df.replace([float('inf'), -float('inf')], np.nan).dropna()

# جایگزینی مقادیر بیش از حد بزرگ به NaN
max_value = 1e12  # عدد بزرگترین حد
df = df.applymap(lambda x: np.nan if isinstance(x, (int, float)) and abs(x) > max_value else x)

# اضافه کردن ویژگی جدید
df['price_to_volume'] = df['current_price'] / df['total_volume']
df['price_to_market_cap'] = df['current_price'] / df['market_cap']

# ایجاد برچسب رشد یا کاهش قیمت (1 برای رشد و 0 برای کاهش)
df['target'] = df['price_change_percentage_24h'].apply(lambda x: 1 if x > 0 else 0)

# انتخاب ویژگی‌ها و هدف
X = df[['current_price', 'market_cap', 'total_volume', 'price_to_volume', 'price_to_market_cap']]
y = df['target']

# مقیاس‌بندی ویژگی‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# تقسیم داده‌ها به مجموعه آموزش و آزمون
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# آموزش مدل
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# پیش‌بینی
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# ذخیره مدل
joblib.dump(model, 'model/random_forest_model.pkl')
print("✅ Model saved to model/random_forest_model.pkl")
