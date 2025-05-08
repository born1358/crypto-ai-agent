import subprocess

print("🚀 Fetching crypto data...")
subprocess.run(["python", "scripts/fetch_data.py"])

print("🧠 Training ML model...")
subprocess.run(["python", "scripts/train_model.py"])

print("🔍 Predicting growing coins...")
subprocess.run(["python", "scripts/predict.py"])

print("📤 Sending predictions to Telegram...")
subprocess.run(["python", "scripts/send_to_telegram.py"])
