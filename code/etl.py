"""
Extract, transform, and/or load data from external sources.
"""
from pathlib import Path

from pandas import DataFrame, read_csv

DATADIR = Path(__file__).resolve().parent.parent / "data"

def rivm(**kwargs):
    """ DataFrame: CoronaWatchNL case counts from RIVM (Dutch health institute). """
    kwargs.setdefault('parse_dates', ['Datum'])
    kwargs.setdefault('index_col', 'Datum')

    data = DataFrame()
    folder = DATADIR / "rivm"
    for col in 'confirmed deceased hospitalized'.split():
        path = (folder / col).with_suffix('.csv')
        data[col] = read_csv(path, **kwargs).pop('Aantal')

    return data.resample('D').sum().astype(int).rename_axis('date')



