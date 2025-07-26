
import threading
import subprocess

def run_bot():
    subprocess.call(["python", "main.py"])

def run_api():
    from api import app
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_api()
