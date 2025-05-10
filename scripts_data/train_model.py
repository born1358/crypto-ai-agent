import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os  # برای بررسی وجود پوشه

# لود داده جدید
df = pd.read_csv("data/top_coins.csv")

# پیش‌پردازش داده‌ها
# حذف مقادیر گمشده
df = df.dropna(subset=['market_cap', 'current_price', 'total_volume', 'price_change_percentage_24h'])

# آماده‌سازی ورودی
df['price_change_24h'] = df['price_change_percentage_24h']
df['target'] = df['price_change_24h'].apply(lambda x: 1 if x > 0 else 0)

X = df[['market_cap', 'current_price', 'total_volume']]
y = df['target']  # هدف (1 = رشد، 0 = کاهش)

# مقیاس‌بندی داده‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# آموزش مدل با Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# بررسی و ایجاد پوشه برای ذخیره مدل
os.makedirs('model', exist_ok=True)

# ذخیره مدل برای استفاده در آینده
joblib.dump(model, 'model/random_forest_model.pkl')

# پیش‌بینی
predictions = model.predict(X_scaled)
df['prediction'] = predictions

# فیلتر: فقط کوین‌هایی که مدل رشد براشون پیش‌بینی کرده
growing_coins = df[df['prediction'] == 1][['name', 'symbol', 'current_price', 'price_change_percentage_24h']]

# ذخیره نتایج پیش‌بینی شده
growing_coins.to_csv("data/growing_coins.csv", index=False)

print("✅ Predictions saved to data/growing_coins.csv")
