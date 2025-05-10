import requests
import pandas as pd

# دریافت داده‌ها از API CoinGecko
def fetch_all_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',  # قیمت‌ها به دلار
        'order': 'market_cap_desc',  # ترتیب بر اساس بازار
        'per_page': 250,  # تعداد کوین‌ها در هر صفحه (می‌توانید این مقدار را تنظیم کنید)
        'page': 1  # صفحه اول
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        print("❌ خطا در دریافت داده‌ها")
        return None

# ذخیره داده‌ها در CSV
def save_to_csv(df):
    df.to_csv('data/all_coins.csv', index=False)
    print("✅ داده‌ها با موفقیت ذخیره شد.")

# اجرای اسکریپت
if __name__ == "__main__":
    df = fetch_all_coins()
    if df is not None:
        save_to_csv(df)
