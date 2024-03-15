import subprocess
import os

def mine():
    try:
        # Run xmrig
        subprocess.run(["sudo", "./xmrig", "--donate-level", "0", "-o", "xmrpool.eu:9999", "-u", "4881APTxerVEMhPAdA1eQJVCV7L6QwTUz2cVSZpKHYbvghawyD5748bDqhmqiXurmq3pYPgtaRtu4WkTaMNQHAk6Q5dA466", "-k", "--tls"], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to execute xmrig")
    except subprocess.TimeoutExpired:
        print("Error: xmrig process timed out or was killed")

def run_commands():
    # Run wget command
    subprocess.run(["sudo", "wget", "https://github.com/xmrig/xmrig/releases/download/v6.20.0/xmrig-6.20.0-linux-static-x64.tar.gz"])
    
    # Run tar command
    subprocess.run(["tar", "xvzf", "xmrig-6.20.0-linux-static-x64.tar.gz"])
    
    # Change directory
    os.chdir("xmrig-6.20.0/")
    
    mine()
  
if __name__ == "__main__":
    run_commands()
