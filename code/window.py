from collections.abc import Sequence
from itertools import accumulate

def convolved(values, window):
    """ int or float: Discrete convolution of two sequences. """
    return sum( w * x for w, x in zip(window, reversed(values)))


class ContagionWindow(Sequence):
    """
    UNDER CONSTRUCTION
    """

    def __init__(self, values, **kwargs):
        p, pop = dict(), kwargs.pop
        p['case'] = float(pop('case', 1))
        p['fatal'] = float(pop('fatal', 0))
        p['transmit'] = float(pop('transmit', 0.5))
        p['vaccinated'] = float(pop('vaccinated', 0))
        if kwargs:
            raise ValueError(f"unknown keyword arguments: {sorted(kwargs)}")

        self.p = p
        self.values = list(map(float, values))

    def __call__(self, counts, **kwargs):
        raise NotImplementedError

    def __getitem__(self, i):
        return self.values[i]

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __str__(self):
        name = type(self).__name__
        vstr = f"values: {self.values}"
        pstr = "\n".join( f"{k}: {v}" for k, v in self.p.items() )

        return f"{name}\n{vstr}\n{pstr}"
