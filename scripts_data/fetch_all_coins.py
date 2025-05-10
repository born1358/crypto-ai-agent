import requests
import pandas as pd

# URL برای درخواست به API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',  # قیمت به دلار
    'order': 'market_cap_desc',  # ترتیب بر اساس مارکت کپ
    'per_page': 250,  # تعداد کوین‌ها در هر صفحه
    'page': 1,  # شماره صفحه
}

# دریافت داده‌ها از API
coins = []
for page in range(1, 6):  # دریافت ۵ صفحه از داده‌ها (مجموعاً ۱۲۰۰ کوین)
    params['page'] = page
    response = requests.get(url, params=params)
    coins.extend(response.json())

# تبدیل داده‌ها به DataFrame
df = pd.DataFrame(coins)

# ذخیره‌سازی داده‌ها
df.to_csv('data/top_coins.csv', index=False)
print("✅ Data saved to data/top_coins.csv")
