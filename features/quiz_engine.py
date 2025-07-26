# features/quiz_engine.py

quiz_data = [
    {
        "question": "ما هو نوع الهجوم الذي يعتمد على إدخال شيفرة SQL ضارة؟",
        "options": ["Phishing", "SQL Injection", "XSS", "Brute Force"],
        "answer": "SQL Injection"
    },
    {
        "question": "أي خوارزمية تستخدم لتشفير البيانات بشكل غير قابل للفك؟",
        "options": ["AES", "RSA", "SHA256", "Base64"],
        "answer": "SHA256"
    },
    {
        "question": "أي طبقة في نموذج OSI تتعامل مع IP Address؟",
        "options": ["Application", "Network", "Transport", "Data Link"],
        "answer": "Network"
    }
]

def get_question(index: int):
    if 0 <= index < len(quiz_data):
        return quiz_data[index]
    else:
        return None
