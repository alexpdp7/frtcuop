#!/usr/bin/env python3
import subprocess
import venv


venv.create(".venv", with_pip=True)
subprocess.run([".venv/bin/pip", "install", "-U", "pip"])
subprocess.run([".venv/bin/pip", "install", "wheel"])
subprocess.run([".venv/bin/pip", "install", "-r", "requirements.txt"])
