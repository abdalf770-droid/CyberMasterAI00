# features/network_utils.py

import ipaddress

def analyze_ip(ip_with_prefix: str) -> str:
    try:
        network = ipaddress.ip_network(ip_with_prefix, strict=False)
        return (
            f"🔍 معلومات الشبكة:\n"
            f"🔸 Network: {network.network_address}\n"
            f"🔸 Broadcast: {network.broadcast_address}\n"
            f"🔸 Netmask: {network.netmask}\n"
            f"🔸 عدد العناوين: {network.num_addresses}\n"
        )
    except Exception as e:
        return f"❌ خطأ في تحليل الشبكة: {str(e)}"

def validate_mac(mac: str) -> str:
    import re
    pattern = r'^([0-9A-Fa-f]{2}[:\-]){5}([0-9A-Fa-f]{2})$'
    return "✅ MAC Address صحيح." if re.match(pattern, mac) else "❌ MAC Address غير صحيح."

def network_auth_info() -> str:
    return (
        "🔐 أنواع المصادقة في الشبكات:\n"
        "- Open Authentication\n"
        "- WPA / WPA2 / WPA3\n"
        "- 802.1X Authentication (RADIUS)\n"
    )
