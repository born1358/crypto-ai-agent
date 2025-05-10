import subprocess

print("🚀 شروع اجرای ایجنت تحلیل بازار کریپتو...")

# 📥 در حال دریافت داده‌ها از بازار
print("📥 در حال دریافت داده‌ها از CoinGecko...")
subprocess.run(["python", "scripts_data/fetch_all_coins.py"], check=True)

# 🤖 در حال آموزش مدل و پیش‌بینی
print("🤖 در حال آموزش مدل و پیش‌بینی...")
subprocess.run(["python", "scripts_data/train_model.py"], check=True)

# 📤 ارسال پیام به تلگرام
print("📤 در حال ارسال نتایج به تلگرام...")
subprocess.run(["python", "scripts_data/send_to_telegram.py"], check=True)

print("✅ همه مراحل با موفقیت اجرا شدند.")
