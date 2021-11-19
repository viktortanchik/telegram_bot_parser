import sys
import subprocess
while (True):
    process = subprocess.Popen([sys.executable, "update.py"])
    process.wait()