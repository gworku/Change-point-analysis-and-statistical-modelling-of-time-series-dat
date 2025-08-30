import sys
from pathlib import Path
# Ensure project root is on sys.path so `src` imports work when script is run
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from src.data_loader import load_all_data
from src.analysis.change_point import detect_change_points


def main():
    prices, events, events_impact = load_all_data()
    print('prices rows:', len(prices))
    print(prices[['brent_price','daily_returns','volatility_30d']].head())
    series = prices['brent_price'].dropna()
    res = detect_change_points(series, method='pelt', model='rbf', n_bkps=3)
    print('change_points:', res['change_points'])
    print('n_segments:', res['n_segments'])
    print('segments:')
    for s in res['segments']:
        print(s)


if __name__ == '__main__':
    main()
