import pandas as pd
import requests
import os

# 🔐 دریافت توکن از محیط
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# بررسی وجود مقادیر
if not BOT_TOKEN or not CHAT_ID:
    raise Exception("❌ توکن یا چت آیدی پیدا نشد. مطمئن شو در GitHub Secrets تعریف شده.")

# 📊 لود داده
df = pd.read_csv("data/growing_coins.csv")

# 📝 ساخت پیام
if df.empty:
    message = "📉 هیچ توکن مستعد رشدی یافت نشد."
else:
    message = "🚀 توکن‌های مستعد رشد:\n\n"
    for _, row in df.iterrows():
        message += f"🪙 {row['name']} ({row['symbol']})\n"
        message += f"💰 قیمت: ${row['current_price']:.2f}\n"
        message += f"📈 تغییر 24h: {row['price_change_percentage_24h']:.2f}%\n\n"

# 📤 ارسال
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}
response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ پیام با موفقیت به تلگرام ارسال شد!")
else:
    print("❌ خطا در ارسال:", response.text)
