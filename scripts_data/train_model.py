import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# لود داده
df = pd.read_csv("data/top_coins.csv")

# ساخت ویژگی‌ها و هدف
df['price_change_24h'] = df['price_change_percentage_24h']
df['target'] = df['price_change_24h'].apply(lambda x: 1 if x > 0 else 0)

X = df[['market_cap', 'current_price', 'total_volume']]
y = df['target']

# استانداردسازی داده‌ها
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# تعریف پارامترهای تستی
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [10, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# اجرای GridSearchCV برای بهترین مدل
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=3,
    n_jobs=-1,
    verbose=2
)

grid_search.fit(X_scaled, y)
best_model = grid_search.best_estimator_

# پیش‌بینی با مدل بهینه
predictions = best_model.predict(X_scaled)
df['prediction'] = predictions

# فیلتر کوین‌هایی که پیش‌بینی رشد دارند
growing_coins = df[df['prediction'] == 1][['name', 'symbol', 'current_price', 'price_change_percentage_24h']]

# ذخیره خروجی
growing_coins.to_csv("data/growing_coins.csv", index=False)
print("✅ Predictions saved to data/growing_coins.csv")
