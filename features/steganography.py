# features/steganography.py

from PIL import Image
import stepic

def hide_text_in_image(image_path: str, text: str, output_path: str) -> str:
    try:
        img = Image.open(image_path)
        encoded_img = stepic.encode(img, text.encode())
        encoded_img.save(output_path, format='PNG')
        return "✅ تم إخفاء النص داخل الصورة بنجاح."
    except Exception as e:
        return f"❌ فشل في الإخفاء: {str(e)}"

def reveal_text_from_image(image_path: str) -> str:
    try:
        img = Image.open(image_path)
        hidden_text = stepic.decode(img)
        return f"📥 النص المخفي: {hidden_text.decode()}"
    except Exception as e:
        return f"❌ فشل في استخراج النص: {str(e)}"
