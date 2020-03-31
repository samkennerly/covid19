"""
Extract, transform, and/or load data from external sources.
"""
from pathlib import Path

from pandas import read_csv

DATADIR = Path(__file__).resolve().parent.parent / "data"

def kaggle():
    raise NotImplementedError

def rivm(path="rivm/report.csv", **kwargs):
    """ DataFrame: Daily new cases from RIVM (Netherlands) PDF report. """
    path = DATADIR / path
    kwargs.setdefault('parse_dates', True)
    kwargs.setdefault('index_col', 'date')

    return read_csv(path, **kwargs).sort_index(axis=1).resample('D').sum()
