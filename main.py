import os
from telegram.ext import MessageHandler, filters
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
from google.generativeai import configure, GenerativeModel
from features.website_scanner import scan_website
from features.fake_terminal import generate_fake_terminal_output
from features.crypto_tools import encrypt, decrypt
from features.multi_language_converter import convert_code
from features.web_vulnerability_scanner import scan_sql_injection
from features.google_dorker import generate_google_dorks
from features.ascii_converter import text_to_ascii, ascii_to_text
from features.code_converter import convert_code_syntax
from features.number_converter import convert_number
from features.network_utils import analyze_ip, validate_mac, network_auth_info
from features.osint_tools import search_breach
from features.tutorials import get_tutorial
from features.quiz_engine import quiz_data


BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

configure(api_key=GEMINI_API_KEY)
gemini_model = GenerativeModel('gemini-pro')
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
# اختيار بين التشفير وفك التشفير
if context.user_data.get("mode") == "choose_encrypt_or_decrypt":
    if "تشفير" in text:
        context.user_data["action"] = "encrypt"
        context.user_data["mode"] = "choose_encryption_type"
    elif "فك التشفير" in text:
        context.user_data["action"] = "decrypt"
        context.user_data["mode"] = "choose_encryption_type"
    else:
        await update.message.reply_text("❗️اختر من الأزرار.")
        return
    
    keyboard = [
        ["🔐 AES", "🔐 Caesar"],
        ["🔐 Base64", "🔐 Vigenère"],
        ["⬅️ رجوع"]
    ]
    await update.message.reply_text("اختر نوع التشفير/فك التشفير:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

# اختيار نوع التشفير
elif context.user_data.get("mode") == "choose_encryption_type":
    algo = text.replace("🔐", "").strip().lower()
    context.user_data["algorithm"] = algo
    
    if context.user_data["action"] == "encrypt":
        context.user_data["mode"] = "encrypt_input"
        await update.message.reply_text(f"✍️ أرسل النص لتشفيره باستخدام {algo.upper()}")
    else:
        context.user_data["mode"] = "decrypt_input"
        await update.message.reply_text(f"✍️ أرسل النص لفك تشفيره باستخدام {algo.upper()}")

    if "تشفير وفك التشفير" in text:
        await update.message.reply_text("🔐 أرسل النص لتشفيره أو لفك التشفير.")
    elif "🔐 التشفير وفك التشفير" in text:
      context.user_data.clear()
      context.user_data["mode"] = "choose_encrypt_or_decrypt"
    
    keyboard = [
        ["🔒 تشفير", "🔓 فك التشفير"],
        ["⬅️ رجوع"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("اختر العملية التي تريد تنفيذها:")

    


    
    elif "تحليل الشبكات" in text:
        await update.message.reply_text("🌐 أرسل عنوان IP مع /24 مثل 192.168.1.1/24")
    
    elif "تحويل أنظمة العد" in text:
        await update.message.reply_text("📊 أرسل الرقم وسيتم تحويله بين (ثنائي - عشري - سداسي).")
    
    elif "تحويل الأكواد" in text:
        await update.message.reply_text("💻 أرسل الكود + اللغة التي تريد التحويل منها وإليها.")
    
    elif "اختبار الأمن السيبراني" in text:
        await update.message.reply_text("🧠 سيتم الآن بدء اختبار الأمن السيبراني...")

    elif "OSINT" in text:
        await update.message.reply_text("🔍 أرسل اسم المستخدم أو الإيميل لفحصه.")

    elif "شروحات الأمن" in text:
        await update.message.reply_text("📚 سيتم عرض الشروحات المتوفرة...")

    else:
        await update.message.reply_text("❗️الأمر غير معروف. اختر من الأزرار.")


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
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.run_polling()


if __name__ == "__main__":
    main()
