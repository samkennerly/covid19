from collections import deque, namedtuple
from itertools import islice, repeat

STATES = (
    "deceased",
    "exposed",
    "infectious",
    "quarantined",
    "recovered",
    "susceptible",
    "vaccinated",
)
Counts = namedtuple("Counts", STATES)

def convolution(values, window):
    """ int or float: Convolution of two sequences. """
    return sum(w * x for w, x in zip(window, reversed(values)))

class Contagion:
    """
    UNDER CONSTRUCTION
    """

    def __init__(self, window, beta=1, fatal=0.5, ilag=0, qlag=1, size=100, vaxrate=0):
        self.beta = float(beta)
        self.fatal = float(fatal)
        self.ilag = int(ilag)
        self.qlag = int(qlag)
        self.size = int(size)
        self.window = list(window)
        self.vaxrate = float(vaxrate)

    def __call__(self, cases, steps=1, **kwargs):
        beta = kwargs.pop("beta", self.beta)
        fatal = kwargs.pop("fatal", self.fatal)
        ilag = kwargs.pop("ilag", self.ilag)
        qlag = kwargs.pop("qlag", self.qlag)
        size = kwargs.pop("size", self.size)
        window = self.window
        vaxrate = kwargs.pop("vaxrate", self.vaxrate)
        if kwargs:
            raise KeyError(f"unknown keyword arguments: {sorted(kwargs)}")

        # Count new cases for each day in window. Pad with zeros if needed.
        rlag = ilag + len(window)
        deltas = (y - x for x, y in zip(cases, cases[1:]))
        deltas = deque(deltas, maxlen=rlag)
        deltas.extendleft(repeat(0, rlag - len(deltas)))
        if any(x < 0 for x in deltas):
            raise ValueError("cases must be a non-decreasing sequence")

        # Initialize counters
        closed = cases[-1] - sum(deltas)
        uninfected = size - cases[-1]
        vaccinated = vaxrate * uninfected
        susceptible = uninfected - vaccinated

        for _ in range(steps):

            delta = tuple(deltas)[ilag : qlag]
            delta = beta * sum(w * x for w, x in zip(reversed(window), delta))
            delta *= susceptible / size
            closed += deltas.popleft()
            deltas.append(delta)

            deceased = fatal * closed
            exposed = sum(islice(deltas, 0, ilag))
            infectious = sum(islice(deltas, ilag, min(qlag, rlag)))
            quarantined = sum(islice(deltas, qlag, rlag))
            recovered = closed - deceased
            susceptible -= delta

            if not susceptible > 0:
                break

            yield Counts(
                deceased,
                exposed,
                infectious,
                quarantined,
                recovered,
                susceptible,
                vaccinated,
            )





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
