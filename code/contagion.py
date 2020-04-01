from collections import deque, namedtuple

STATES = (
    "deceased",
    "exposed",
    "infectious",
    "quarantined",
    "recovered",
    "susceptible",
    "vaccinated",
)


def convolution(values, window):
    """ int or float: Convolution of two sequences. """
    return sum(w * x for w, x in zip(window, reversed(values)))


class Contagion:
    """
    UNDER CONSTRUCTION
    """
    Counts = namedtuple("Counts", STATES)

    def __init__(self, window=None, **kwargs):
        window = tuple(map(float, window))
        params = {
            "beta": float(kwargs.pop("beta", 1.0)),
            "dprob": float(kwargs.pop("dprob", 0.1)),
            "dtime": int(kwargs.pop("dtime", len(window))),
            "qprob": float(kwargs.pop("qprob", 0.5)),
            "qtime": int(kwargs.pop("qtime", len(window))),
            "total": int(kwargs.pop("total", 100)),
            "vprob": float(kwargs.pop("vprob", 0.0)),
        }
        if kwargs:
            raise ValueError(f"unknown keyword arguments: {sorted(kwargs)}")

        self.params = params
        self.window = window

    def __call__(self, deltas, **kwargs):
        params = {**self.params, **kwargs}
        window = self.window

        wtime = len(window)


        exposed = s * sum(w * x for w, x in zip(reversed(window), values))

        delayed = deltas[-wtime] if (len(deltas) > tau) else 0

        deceased = int(mu * delayed)
        recovered = delayed - deceased

        infectious = convolution(deltas, *(w > 0 for w in window))
        quarantined = convolution(deltas, *(w == 0 for w in window))

        vaccinated = int(vax_rate * unexposed)
        susceptible = unexposed - vaccinated

        return deceased, recovered, infectious, quarantined, susceptible, vaccinated

    def __repr__(self):
        name = type(self).__name__
        argstr = ", ".join(map(str, self.window))
        kwargstr = ", ".join( f"{k}={v}" for k, v in self.params.items() )

        return f"{name}({argstr}, {kwargstr})"




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
