from collections import deque, namedtuple
from itertools import chain, islice, repeat, takewhile

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


class Window:
    """
    UNDER CONSTRUCTION
    """

    def __init__(self, *args, delay=None, escape=0, fatal=0, size=1, vax=0):
        self.betas = list(map(float, args))
        self.delay = len(args) if delay is None else int(delay)
        self.escape = float(escape)
        self.fatal = float(fatal)
        self.size = float(size)
        self.vax = float(vax)

    def __call__(self, *args, **kwargs):
        return type(self)(*(args or self.betas), **{**self.params, **kwargs})

    def __iter__(self):
        betas, delay, escape = self.betas, self.delay, self.escape

        return chain(betas[:delay], (escape * x for x in betas[delay:]))

    def __len__(self):
        return len(self.betas)

    def __mul__(self, scalar):
        return self(*(scalar * x for x in self.betas))

    def __repr__(self):
        return f"{type(self).__name__}{tuple(self)}"

    def __reversed__(self):
        return reversed(tuple(self))

    def __truediv__(self, scalar):
        return self * (1.0 / scalar)

    def forecast(self, cases, limit=1):
        """ Iterable[Counts]: Predicted counts on each future timestep. """
        escape = self.escape
        fatal = self.fatal
        gap = self.gap
        latency = self.latency
        size = self.size
        vax = self.vax

        cases = deque(cases, maxlen=len(self))
        deltas = deque(y - x for x, y in zip((0, *cases), cases))
        deltas.extend(repeat(0, len(self) - len(deltas)))
        closed = cases[-1] - sum(deltas)
        vaccinated = vax * size
        susceptible = size - cases[-1] - vaccinated

        for _ in range(limit):

            delta = sum(w * x for w, x in zip(self, deltas))
            delta = min(susceptible, delta * susceptible / size)
            closed += deltas.pop()
            deltas.appendleft(delta)

            deceased = fatal * closed
            recovered = closed - deceased
            susceptible -= delta

            quarantined = sum(islice(deltas, latency + gap, None)) * (1 - escape)
            infectious = sum(islice(deltas, latency, None)) - quarantined
            exposed = sum(islice(deltas, 0, latency))

            yield Counts(
                deceased,
                exposed,
                infectious,
                quarantined,
                recovered,
                susceptible,
                vaccinated,
                )

    @property
    def gap(self):
        """ int: Time between host becoming infectious and quarantine start. """
        return max(0, self.delay - self.latency)

    @property
    def latency(self):
        """ int: Timestep after exposure when host becomes infectious. """
        return sum(1 for _ in takewhile(lambda x: not x, self.betas))

    @property
    def params(self):
        """ dict: All keyword arguments needed to create a copy. """
        keys = "delay escape fatal size vax".split()

        return {k: getattr(self, k) for k in keys}

    @property
    def ratio(self):
        """ float: Reproduction ratio. """
        return sum(self)


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
