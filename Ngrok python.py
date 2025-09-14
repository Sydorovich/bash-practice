import subprocess
import time
import requests

# Start ngrok tunnel to port 8188
ngrok_process = subprocess.Popen(['./ngrok', 'http', '8188'],
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.STDOUT)

# Wait and retry connection
for i in range(10):
    try:
        r = requests.get('http://localhost:4040/api/tunnels')
        public_url = r.json()['tunnels'][0]['public_url']
        print(f"✅ Ngrok tunnel established: {public_url}")
        break
    except Exception as e:
        print(f"⏳ Attempt {i+1}/10: Ngrok not ready yet...")
        time.sleep(2)
else:
    print("❌ Ngrok failed to start. Please restart the runtime and try again.")
