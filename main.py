import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
from google.generativeai import configure, GenerativeModel
from features.website_scanner import scan_website
from features.fake_terminal import generate_fake_terminal_output
from features.crypto_tools import encrypt, decrypt
from features.multi_language_converter import convert_code
from features.web_vulnerability_scanner import scan_sql_injection
from features.google_dorker import generate_google_dorks
from features.ascii_converter import to_ascii, from_ascii
from features.code_converter import convert_syntax
from features.number_converter import convert_number
from features.network_utils import analyze_ip, subnet_mask
from features.osint_tools import analyze_ip_address
from features.tutorials import get_tutorial
from features.quiz_engine import start_quiz


BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

configure(api_key=GEMINI_API_KEY)
gemini_model = GenerativeModel('gemini-pro')

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("✍️ أرسل سؤالك بعد الأمر /ask")
        return
    response = gemini_model.generate_content(prompt)
    await update.message.reply_text(response.text)

async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🔍 أرسل رابط الموقع بعد /scan")
        return
    domain = context.args[0]
    result = scan_website(domain)
    await update.message.reply_text(f"نتيجة الفحص:\n{result}")



async def hack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    terminal_output = generate_fake_terminal_output()
    await update.message.reply_text(f"💻 Fake Terminal Output:\n{terminal_output}")

    terminal_output = generate_fake_terminal_output()
   await update.message.reply_text(f"💻 Fake Terminal Output:\n{terminal_output}")

def main():
    print("🚀 CyberMaster AI is starting...")
    
from telegram import ReplyKeyboardMarkup

main_buttons = [
    ["🔐 التشفير وفك التشفير", "🖼️ الإخفاء داخل الصور"],
    ["🧠 أدوات OSINT", "🌐 تحليل الشبكات"],
    ["🔄 تحويل الأكواد", "🧮 تحويل أنظمة العد"],
    ["📜 شروحات الأمن", "🧪 اختبار الأمن السيبراني"],
    ["🎭 محاكي اختراق وهمي", "🧰 أدوات أخرى"]
]

main_keyboard = ReplyKeyboardMarkup(main_buttons, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحباً بك في CyberMaster AI\nاختر الخدمة التي تريدها:",
        reply_markup=main_keyboard
    )


app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("hack", hack))
    app.run_polling()

if __name__ == "__main__":
    main()
