import sys
import pathlib
import numpy as np
import pandas as pd

# Add repository root (the folder that contains 'src') to sys.path
p = pathlib.Path(__file__).resolve()
# start from the scripts directory
root = p.parent
# The repo's actual code lies one level down in the folder named
# 'Change-point-analysis-and-statistical-modelling-of-time-series-dat'
candidate = root / 'Change-point-analysis-and-statistical-modelling-of-time-series-dat'
if candidate.exists() and (candidate / 'src').exists():
    root = candidate
else:
    # also try from the current working directory (when script run from project root)
    cwd_candidate = pathlib.Path.cwd() / 'Change-point-analysis-and-statistical-modelling-of-time-series-dat'
    if cwd_candidate.exists() and (cwd_candidate / 'src').exists():
        root = cwd_candidate
    else:
        # try climbing parents
        temp = root
        while not (temp / 'src').exists() and temp.parent != temp:
            temp = temp.parent
        if (temp / 'src').exists():
            root = temp
        else:
            # search recursively for any `src` directory and take its parent
            found = None
            for p in root.rglob('src'):
                if p.is_dir():
                    found = p.parent
                    break
            if found is not None:
                root = found
if (root / 'src').exists():
    sys.path.insert(0, str(root))
    print('Inserted to sys.path:', str(root))
else:
    print('Could not find repo root containing src; checked:', root)
    print('Directory listing of current folder:', list(pathlib.Path('.').iterdir()))
    raise SystemExit('src package not found; aborting')

from src.analysis.change_point import ChangePointDetector

np.random.seed(0)

n = 100
rng = pd.date_range('2020-01-01', periods=n)
data = np.concatenate([np.random.normal(0, 1, 50), np.random.normal(5, 1, 50)])
series = pd.Series(data, index=rng)

det = ChangePointDetector()
print('series std:', np.std(data))
print('detect_simple:', det._detect_simple(series, n_bkps=1))
print('detect_cusum (default params):', det._detect_cusum(series, n_bkps=1))
print('detect_cusum (sensitive):', det._detect_cusum(series, n_bkps=1, threshold=None, drift=0.0, max_iter=50))
