from hijri_converter import Gregorian
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import pytz

# Command handler for /start and /hijri
async def show_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get current India time
    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)

    # Gregorian date and time with seconds
    english_date = now.strftime("%d %B %Y")
    time_now = now.strftime("%I:%M:%S %p")  # With seconds

    # Hijri date
    hijri = Gregorian(now.year, now.month, now.day).to_hijri()
    hijri_date = f"{hijri.day} {hijri.month_name()} {hijri.year} AH"

    # Final message with bold heading
    message = (
        "*📢 Assalamualaikum - This bot is created by Muhammad Alqama*\n"
        "*🇮🇳 Made with ❤️ from INDIA*\n\n"
        f"🗓️ *English Date:* {english_date}\n"
        f"🕌 *Islamic Date:* {hijri_date}\n"
        f"🕰️ *Indian Time:* {time_now}"
    )

    await update.message.reply_text(message, parse_mode="Markdown")

# Bot setup
app = ApplicationBuilder().token("8003003944:AAHcJRUkSmUoiItZ_2qpRE9y6uRkPYhwZg4").build()
app.add_handler(CommandHandler("start", show_date))
app.add_handler(CommandHandler("hijri", show_date))

print("📅 Islamic Calendar Bot is running...")
app.run_polling()
