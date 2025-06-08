from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ВСТАВЬ СВОЙ ТОКЕН ОТ @BotFather
BOT_TOKEN = "7662046816:AAFlVSYrR3Swnk055GTs_9cDmztfueZgnwk"

# ВСТАВЬ СЮДА ССЫЛКУ НА СВОЮ HTML-СТРАНИЦУ (например, с Netlify)
WEBAPP_URL = "https://myweb-woad.vercel.app/"

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        KeyboardButton(
            text="🧠 Открыть мини-приложение",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.message.reply_text(
        "Привет! Жми на кнопку, чтобы открыть мини-приложение 👇",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ Бот запущен...")
app.run_polling()
