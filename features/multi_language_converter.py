def convert_code(code: str, from_lang: str, to_lang: str) -> str:
    """
    تحويل كود برمجي بسيط من لغة إلى أخرى (مبسط - قواعد يدوية)
    """
    if from_lang == "python" and to_lang == "javascript":
        return code.replace("print(", "console.log(").replace(")", ");")
    elif from_lang == "javascript" and to_lang == "python":
        return code.replace("console.log(", "print(").replace(");", ")")
    elif from_lang == "python" and to_lang == "c":
        return "#include <stdio.h>\nint main() {\n    printf(" + code.split("print(")[-1].rstrip(")") + ");\n    return 0;\n}"
    elif from_lang == "c" and to_lang == "python":
        return "print(" + code.split("printf(")[-1].split(");")[0] + ")"
    else:
        return "⚠️ التحويل غير مدعوم بعد بين هذه اللغتين."