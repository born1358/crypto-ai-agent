import pandas as pd
import numpy as np

# بارگذاری داده‌ها
df = pd.read_csv('data/top_coins.csv')

# فیلتر کردن داده‌های معتبر
df = df[['id', 'symbol', 'name', 'current_price', 'price_change_percentage_24h', 'market_cap', 'total_volume']]
df = df.dropna()  # حذف داده‌های خالی

# تبدیل مقادیر به عددی (در صورت وجود مقادیر متنی)
df['current_price'] = pd.to_numeric(df['current_price'], errors='coerce')
df['price_change_percentage_24h'] = pd.to_numeric(df['price_change_percentage_24h'], errors='coerce')
df['market_cap'] = pd.to_numeric(df['market_cap'], errors='coerce')
df['total_volume'] = pd.to_numeric(df['total_volume'], errors='coerce')

# حذف ستون‌هایی که به اشتباه به صورت متنی تبدیل شده‌اند
df = df.apply(pd.to_numeric, errors='coerce')

# چاپ مقادیر غیرمجاز (infinity یا بیش از حد بزرگ)
print("Check for infinity or large values:")
print(df[(df > 1e12) | (df < -1e12)])

# جایگزینی مقادیر بیش از حد بزرگ به NaN
max_value = 1e12
df = df.applymap(lambda x: np.nan if isinstance(x, (int, float)) and abs(x) > max_value else x)

# حذف مقادیر NaN
df = df.dropna()

# اضافه کردن ویژگی جدید
df['price_to_volume'] = df['current_price'] / df['total_volume']

# ذخیره داده‌های تمیز شده
df.to_csv('data/cleaned_top_coins.csv', index=False)

# ادامه کارهای مدل (آموزش و پیش‌بینی)
