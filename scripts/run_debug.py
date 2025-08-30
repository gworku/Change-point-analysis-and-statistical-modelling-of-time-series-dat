import sys
from pathlib import Path
print('cwd:', Path.cwd())
print('__file__:', Path(__file__).resolve())
print('sys.path[:5]:', sys.path[:5])
print('Listing project root:', list(Path.cwd().iterdir()))

# Try to import src
try:
    import src
    print('Imported src OK, src.__path__ =', getattr(src, '__path__', None))
except Exception as e:
    print('Import src failed:', type(e), e)

# Add project root to sys.path and try again
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))
print('Inserted project_root to sys.path:', project_root)
try:
    import src
    print('Imported src after insert OK, src.__path__ =', getattr(src, '__path__', None))
except Exception as e:
    print('Import src after insert failed:', type(e), e)
