import os

TEXT_PORT = 8080
TEXT_SERVER = os.getenv("BACKEND_TEXT", "0.0.0.0")
TOP_k=10
MODEL = "en_core_web_md"
WORKSPACE_DIR = "workspace"
CACHE_DIR = os.path.expanduser('~/.cache')