# features/user_requests.py

requests_log = []

def log_user_request(user_id: int, topic: str) -> str:
    try:
        requests_log.append((user_id, topic))
        return "✅ تم استلام طلبك، سيتم إضافة الشرح قريبًا."
    except Exception as e:
        return f"❌ فشل في تسجيل الطلب: {str(e)}"

def get_all_requests() -> list:
    return requests_log
