# contagion window models

## UNDER CONSTRUCTION

## abstract

Contagion window models are designed to forecast large-scale infections with time-sensitive transmission probabilities. Infected nodes are grouped by the day on which their infections began, and the infectiousness of each group depends on how long it has been infected.

A daily contagion [window] is a vector $\mathbf{w}$ whose components $w_i$ are estimated mean transmission counts for a node $i$ days after it is infected. Like $\beta$ in a [SIR model], window counts can be influenced by the collective behaviors of individual nodes. Unlike SIR models, discrete window models obey a difference equation.

[window]: https://en.wikipedia.org/wiki/Window_function
[SIR model]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SIR_model
[convolution]: https://en.wikipedia.org/wiki/Convolution

## constants

## definitions

## evolution

Time evolution of $x_t$ is governed by a [master equation]:
$$
x_{t+1} = \frac{S_t}{N}(\mathbf{w} * \mathbf{x})_t
$$
where <dfn>susceptiblility</dfn> term is the fraction of nodes which are neither vaccinated nor exposed:
$$
\frac{S_t}{N}
= \frac{N(1-v) - X_t}{N}
= 1 - v - \frac{1}{N}\sum_{i=0}^{t-1} x_i
$$
and the <dfn>contagion</dfn> term is the sum of recent daily infections weighted by window counts:
$$
(\mathbf{w} * \mathbf{x})_t
= \sum_{i=-\infty}^{\infty} w_i x_{t-i}
= w_0 x_t + w_1 x_{t-1} + \cdots + w_{\tau-1}x_{t-(\tau-1)}
= \sum_{i=0}^{\tau-1} w_i x_{t-i}
$$


[master equation]: https://en.wikipedia.org/wiki/Master_equation

## scenarios

### count the days

{natural window with citations}

### flatten the curve

{reduce $|\mathbf{w}|$ by decreasing contact frequency}

### close the window

In this scenario, infectious nodes quarantine themselves when symptoms present. This strategy is effective if and only if nodes become infectious *after* symptoms become obvious.

<blockquote>
Many (especially young people) might not notice any symptoms at all, or very mild symptoms. Then they don’t know they have the virus and can pass it on to people in risk groups.
<br><cite>Greta Thunberg</cite>
</blockquote>

### slam the brakes

If nodes become infections *before* symptoms become obvious, then "closing the window" may be insufficient to halt an epidemic.

### kill the virus

{no eradication without vaccination}

### don't wait and see

### don't jump the gun

