from collections import namedtuple
from collections.abc import Sequence
from itertools import accumulate

STATES = (
    "deceased",
    "infectious",
    "quarantined",
    "recovered",
    "susceptible",
    "vaccinated",
)


class ContagionWindow(Sequence):
    """
    UNDER CONSTRUCTION
    """

    Counts = namedtuple("Counts", ["confirmed", *STATES])

    def __init__(self, values, **kwargs):
        self.values = list(map(float, values))
        self.p = {
            "confirm": float(kwargs.pop("case", 0.9)),
            "fatal": float(kwargs.pop("fatal", 0.1)),
            "vax": float(kwargs.pop("vax", 0)),
        }

        if kwargs:
            raise ValueError(f"unknown keyword arguments: {sorted(kwargs)}")

    def __call__(self, cases, **kwargs):

        tau = len(window)

        exposed = (1 - vax_rate - sum(deltas) / n) * convolved(deltas, window)

        delayed = deltas[-tau] if (len(deltas) > tau) else 0
        unexposed = n - sum(deltas)

        deceased = int(mu * delayed)
        recovered = delayed - deceased

        infectious = convolved(deltas, *(w > 0 for w in window))
        quarantined = convolved(deltas, *(w == 0 for w in window))

        vaccinated = int(vax_rate * unexposed)
        susceptible = unexposed - vaccinated

        return deceased, recovered, infectious, quarantined, susceptible, vaccinated

    def __getitem__(self, i):
        return self.values[i]

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return f"{type(self).__name__}{tuple(self.values)}"

    def __str__(self):
        return "\n".join([repr(self), *(f"{k}: {v}" for k, v in self.p.items())])

    def convolved(values, window):
        return sum(w * x for w, x in zip(window, reversed(values)))


# Copyright © 2020 Sam Kennerly
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
