# Honestly, not so sure how if I'm going to write this to anyone else
# For my own use case I guess this is good.

import sys
import os
from pathlib import Path

assert len(sys.argv) == 2

INSTALL_PATH = sys.argv[1]
PROJECT_DIR = Path(__file__).resolve().parent
SCRIPT_PATH = f"{INSTALL_PATH}/todo"

with open(SCRIPT_PATH, "w") as f:
    f.write("#!/usr/bin/sh\n")
    f.write("\n")
    f.write(f"python3 {PROJECT_DIR}/todo.py \"$@\"\n")

os.chmod(SCRIPT_PATH, 0o755)
