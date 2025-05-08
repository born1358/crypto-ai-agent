import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# لود داده
df = pd.read_csv("data/top_coins.csv")

# انتخاب ویژگی‌ها
df['price_change_24h'] = df['price_change_percentage_24h']
df['target'] = df['price_change_24h'].apply(lambda x: 1 if x > 0 else 0)  # رشد داشته یا نه؟

X = df[['market_cap', 'current_price', 'total_volume']]
y = df['target']

# آماده‌سازی داده
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# آموزش مدل
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# نمایش دقت
accuracy = model.score(X_test, y_test)
print(f"✅ Model accuracy: {accuracy:.2f}")
