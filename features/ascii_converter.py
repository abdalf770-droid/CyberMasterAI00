def text_to_ascii(text: str) -> str:
    try:
        ascii_values = [str(ord(char)) for char in text]
        return ' '.join(ascii_values)
    except Exception as e:
        return f"❌ خطأ في التحويل إلى ASCII: {str(e)}"

def ascii_to_text(ascii_code: str) -> str:
    try:
        chars = [chr(int(code)) for code in ascii_code.split()]
        return ''.join(chars)
    except Exception as e:
        return f"❌ خطأ في التحويل من ASCII إلى نص: {str(e)}"
