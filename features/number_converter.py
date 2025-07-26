# features/number_converter.py

def convert_number(value: str, base_from: str, base_to: str) -> str:
    try:
        base_map = {
            "binary": 2,
            "decimal": 10,
            "octal": 8,
            "hex": 16
        }

        if base_from not in base_map or base_to not in base_map:
            return "❌ نظام العد غير مدعوم."

        num = int(value, base_map[base_from])
        if base_to == "binary":
            return bin(num)[2:]
        elif base_to == "decimal":
            return str(num)
        elif base_to == "octal":
            return oct(num)[2:]
        elif base_to == "hex":
            return hex(num)[2:].upper()
    except Exception as e:
        return f"❌ خطأ في التحويل: {str(e)}"
