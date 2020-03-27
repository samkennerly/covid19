from collections.abc import Sequence


def convolved(values, window):
    """ int or float: Discrete convolution of two sequences. """
    return sum( w * x for w, x in zip(window, reversed(values)))


class ContagionWindow(Sequence):
    """
    UNDER CONSTRUCTION
    """

    def __init__(self, values=(1,), **kwargs):
        probs, pop = dict(), kwargs.pop
        probs['case'] = float(pop('case', 1))
        probs['fatal'] = float(pop('p_fatal', 0))
        probs['transmit'] = float(pop('p_transmit', 0.5))
        probs['vaccinate'] = float(pop('p_vaccinate', 0))
        if kwargs:
            raise ValueError(f"unknown keyword arguments: {sorted(kwargs)}")

        self.probs = probs
        self.values = tuple(map(float, values))

    def __getitem__(self, i):
        return self.values[i]

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return "\n".join(str(self.values), *[ f"{k}: {v}" for k, v in self.probs ])



