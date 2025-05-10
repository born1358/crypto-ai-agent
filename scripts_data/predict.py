import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# لود داده جدید
df = pd.read_csv("data/top_coins.csv")

# آماده‌سازی ورودی
df['price_change_24h'] = df['price_change_percentage_24h']
df['target'] = df['price_change_24h'].apply(lambda x: 1 if x > 0 else 0)

X = df[['market_cap', 'current_price', 'total_volume']]
y = df['target']  # واقعی (فعلاً برای تست دقت)

# آموزش مدل روی همین داده‌ها (به‌جای لود مدل ذخیره‌شده، برای سادگی فعلاً باز آموزش می‌دیم)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression()
model.fit(X_scaled, y)

# پیش‌بینی
predictions = model.predict(X_scaled)
df['prediction'] = predictions

# فیلتر: فقط کوین‌هایی که مدل رشد براشون پیش‌بینی کرده
growing_coins = df[df['prediction'] == 1][['name', 'symbol', 'current_price', 'price_change_percentage_24h']]

# نمایش
print("🔮 Coins predicted to grow:")
print(growing_coins)

# ذخیره خروجی
growing_coins.to_csv("data/growing_coins.csv", index=False)
print("✅ Predictions saved to data/growing_coins.csv")
