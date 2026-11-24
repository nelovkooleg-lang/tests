import sys
from pathlib import Path

ROOT_DIR = path(__file__).resolve().parent
TESTS_DIR = ROOT_DIR / 'tests'

if str(ROOT_DIR) not in sys.path:
  sys.path.insert(0, str(ROOT_DIR))
if TESTS_DIR.exists() and str(TESTS_DIR) not in sys.path:
  sys.path.insert(0, str(TESTS_DIR))
