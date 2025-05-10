# run_all.py

import subprocess

print("🚀 شروع اجرای ایجنت تحلیل بازار کریپتو...")

# اجرای مرحله 1: دریافت داده‌ها
print("\n📥 در حال دریافت داده‌ها از بازار...")
subprocess.run(["python", "scripts data/fetch_data.py"], check=True)

# اجرای مرحله 2: آموزش و پیش‌بینی با مدل RandomForest
print("\n🤖 در حال آموزش مدل و پیش‌بینی...")
subprocess.run(["python", "scripts data/train_model.py"], check=True)

# اجرای مرحله 3: ارسال نتیجه به تلگرام
print("\n📤 ارسال نتایج به تلگرام...")
subprocess.run(["python", "scripts data/send_to_telegram.py"], check=True)

print("\n✅ همه مراحل با موفقیت انجام شد.")
