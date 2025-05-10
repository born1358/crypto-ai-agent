import subprocess
import joblib

print("🚀 شروع اجرای ایجنت تحلیل بازار کریپتو...")

# مرحله 1: دریافت داده‌ها
print("\n📥 در حال دریافت داده‌ها از بازار...")
subprocess.run(["python", "scripts_data/fetch_data.py"], check=True)

# مرحله 2: آموزش مدل و پیش‌بینی
print("\n🤖 در حال آموزش مدل و پیش‌بینی...")
subprocess.run(["python", "scripts_data/train_model.py"], check=True)

# مرحله 3: ارسال نتایج به تلگرام
print("\n📤 ارسال نتایج به تلگرام...")
subprocess.run(["python", "scripts_data/send_to_telegram.py"], check=True)

print("\n✅ همه مراحل با موفقیت انجام شد.")
