import random

def generate_fake_terminal_output():
    messages = [
        "[+] Connecting to target...",
        "[+] Handshake successful.",
        "[+] Bypassing firewall...",
        "[+] Exploit launched...",
        "[+] Dumping credentials...",
        "[+] Access granted!",
        "[*] Session terminated."
    ]
    output = "\n".join(random.sample(messages, k=len(messages)))
    return output
