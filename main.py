import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # <-- загружает .env

BOT_TOKEN = os.getenv("8231730889:AAHNS3AZNJPkrgX6GLd4fDBl2v1wSQwRsYA")
USER_ID = os.getenv("7637653316")
USERNAME = os.getenv("giggerr")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 20))

def is_available(username):
    url = f"https://t.me/{username}"
    r = requests.get(url, allow_redirects=True)
    return "If you have Telegram" in r.text or r.status_code == 404

def notify(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": USER_ID, "text": text})

print("Monitor started...")

while True:
    try:
        if is_available(USERNAME):
            notify(f"🔥 Username @{USERNAME} свободен!")
        time.sleep(CHECK_INTERVAL)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(5)
