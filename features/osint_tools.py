import requests

def search_breach(email):
    try:
        response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", headers={"hibp-api-key": "YOUR_API_KEY"})
        if response.status_code == 200:
            return "⚠️ تم العثور على تسريبات لهذا البريد!"
        elif response.status_code == 404:
            return "✅ لا توجد تسريبات لهذا البريد."
        else:
            return f"❌ حدث خطأ: {response.status_code}"
    except Exception as e:
        return str(e)

def ip_lookup(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"🔎 الدولة: {r.get('country')}\nالمدينة: {r.get('city')}\nمقدم الخدمة: {r.get('isp')}"
    except:
        return "❌ تعذر استرجاع المعلومات."