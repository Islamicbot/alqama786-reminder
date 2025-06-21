from hijri_converter import Gregorian
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import pytz

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "**Assalamualaikum - This Bot is Created by Muhammad Alqama (Made with ❤️ from INDIA)**\n"
        "Type /hijri to get today’s date and time."
    )

# /hijri command
async def hijri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)
    gregorian = now.strftime("%d %B %Y")
    time_now = now.strftime("%I:%M:%S %p")
    hijri_date = Gregorian(now.year, now.month, now.day).to_hijri()
    hijri_str = f"{hijri_date.day} {hijri_date.month_name()} {hijri_date.year} AH"
    message = (
        "**📅 Islamic Calendar Bot**\n\n"
        f"🗓️ Gregorian Date: {gregorian}\n"
        f"🕌 Hijri Date: {hijri_str}\n"
        f"🕰️ Indian Time: {time_now}"
    )
    await update.message.reply_text(message)

app = ApplicationBuilder().token("PASTE-YOUR-TOKEN-HERE").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hijri", hijri))

print("📅 Islamic Calendar Bot is running...")
app.run_polling()
