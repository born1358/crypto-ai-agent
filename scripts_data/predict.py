import pandas as pd
import joblib

# بارگذاری مدل
model = joblib.load('model/random_forest_model.pkl')

# بارگذاری داده‌ها
df = pd.read_csv('data/top_coins.csv')

# پیش‌پردازش داده‌ها
df = df[['id', 'symbol', 'name', 'current_price', 'price_change_percentage_24h', 'market_cap', 'total_volume']]
df = df.dropna()

# اضافه کردن ویژگی جدید
df['price_to_volume'] = df['current_price'] / df['total_volume']
df['price_to_market_cap'] = df['current_price'] / df['market_cap']

# انتخاب ویژگی‌ها
X = df[['current_price', 'market_cap', 'total_volume', 'price_to_volume', 'price_to_market_cap']]

# پیش‌بینی
predictions = model.predict(X)
df['prediction'] = predictions

# فیلتر کردن کوین‌هایی که پیش‌بینی رشد دارند
growing_coins = df[df['prediction'] == 1][['name', 'symbol', 'current_price', 'price_change_percentage_24h']]

# ذخیره پیش‌بینی‌ها
growing_coins.to_csv('data/growing_coins.csv', index=False)
print("✅ Predictions saved to data/growing_coins.csv")
