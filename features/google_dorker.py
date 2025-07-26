def generate_google_dorks(domain):
    dorks = [
        f"site:{domain} intitle:index.of",
        f"site:{domain} inurl:admin",
        f"site:{domain} ext:sql | ext:xml | ext:json",
        f"site:{domain} confidential",
    ]
    return "\n".join(dorks)