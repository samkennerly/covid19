"""
Extract, transform, and/or load data from external sources.
"""
from pathlib import Path

from pandas import read_csv

DATADIR = Path(__file__).resolve().parent.parent / "data"

def kaggle(path="kaggle/global/input/train.csv", **kwargs):
    """ DataFrame: Daily total cases from Kaggle Global Forecasting contest. """
    kwargs.setdefault('parse_dates', ['Date'])
    kwargs.setdefault('index_col', 'Country_Region Province_State Date'.split())

    return (
        read_csv(DATADIR / path, **kwargs)
        .rename(columns={'ConfirmedCases': 'confirmed', 'Fatalities': 'deceased'})
        .drop(columns='Id').astype(int)
    )

def rivm(path="rivm/report.csv", **kwargs):
    """ DataFrame: Daily new cases from RIVM (Netherlands) PDF report. """
    kwargs.setdefault('parse_dates', ['date'])
    kwargs.setdefault('index_col', 'date')

    return (
        read_csv(DATADIR / path, **kwargs)
        .rename_axis(None).sort_index(axis=1)
        .resample('D').sum().astype(int)
    )
