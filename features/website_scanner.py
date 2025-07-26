
import socket
import whois
import requests
from urllib.parse import urlparse

def scan_website(domain):
    result = []

    try:
        # استخراج IP
        ip = socket.gethostbyname(domain)
        result.append(f"🔍 IP Address: {ip}")
    except Exception as e:
        result.append(f"❌ IP Error: {e}")

    try:
        # معلومات Whois
        whois_info = whois.whois(domain)
        registrar = whois_info.registrar or "غير معروف"
        creation_date = whois_info.creation_date or "غير معروف"
        result.append(f"📄 Registrar: {registrar}")
        result.append(f"📅 Creation Date: {creation_date}")
    except Exception as e:
        result.append(f"❌ Whois Error: {e}")

    try:
        # الطلب للرأس
        response = requests.get(f"http://{domain}", timeout=5)
        result.append(f"✅ Status Code: {response.status_code}")
        headers = response.headers
        if 'Server' in headers:
            result.append(f"🖥 Server: {headers['Server']}")
        if 'X-Powered-By' in headers:
            result.append(f"⚙️ Powered By: {headers['X-Powered-By']}")
    except Exception as e:
        result.append(f"❌ HTTP Error: {e}")

    # كلمات خطرة قد تشير إلى ثغرات
    suspicious_words = ["admin", "login", "php?id=", "sql", "select", "alert(", "<script>"]
    try:
        content = requests.get(f"http://{domain}", timeout=5).text.lower()
        for word in suspicious_words:
            if word in content:
                result.append(f"⚠️ Found possible vulnerability hint: '{word}'")
    except Exception:
        pass

    return "\n".join(result)
