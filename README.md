# contagion window models

## UNDER CONSTRUCTION

## abstract

Contagion window models simulate [viral phenomena] with time-dependent [transmission] probabilities. The example shown here evolves according to a discrete [difference equation], not a differential equation.

Each [window] is a sequence **w** such that each element <i>w<sub>i</sub></i> is the expected number of transmissions from one node after *i* days of infection. Like 𝛽 in a [SIR model], window elements represent averaged behavior of many individual nodes. Quarantine after *q* days of infection is modeled by setting <i>w<sub>i</sub></i> = 0 for all *i* &gt; *q*. Reduced transmission probability and/or [social distancing] is modeled by decreasing window magnitude |**w**|.

The examples shown here use [finite-response] windows with fixed duration. Each node is assumed to die or become permanently immune after 𝜏 days. The infection duration 𝜏 must be estimated experimentally.

THE EXAMPLES HERE ARE NOT MEDICAL ADVICE. The author is a [quant], not an epidemiologist.

[viral phenomena]: https://en.wikipedia.org/wiki/Viral_phenomenon
[transmission]: https://en.wikipedia.org/wiki/Transmission_(medicine)
[difference equation]: https://en.wikipedia.org/wiki/Recurrence_relation
[window]: https://en.wikipedia.org/wiki/Window_function
[SIR model]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
[finite-response]: https://en.wikipedia.org/wiki/Finite_impulse_response


[quant]: https://en.wikipedia.org/wiki/Quantitative_analysis_(finance)

[social distancing]: https://en.wikipedia.org/wiki/Social_distancing

## scenarios

### count the days

{natural window with citations}

### flatten the curve

{reduce |**w**| by decreasing contact frequency}

### close the window

In this scenario, nodes quarantine themselves when they learn they are infected. To minimize new infections, *nodes must know when they become infectious.* If symptoms are not obvious before transmission is possible, then nodes may not be able to "close the window" quickly enough.

<blockquote>
Many people don’t feel symptoms at all, or very mild symptoms, but it can still be contagious. So you have to really practice social distancing whether you feel ill or not.<br>
<cite>
<a href="https://www.newscientist.com/article/2238364-greta-thunberg-says-she-may-have-had-covid-19-and-has-self-isolated/#ixzz6HwUUMKx4">
Greta Thunberg</a>
</cite>
</blockquote>

### hit the brakes

To stop [subclinical] transmissions, infectious nodes must be quarantined regardless of symptoms. Without accurate tests, it may be necessary to anticipate possible infections and quarantine pre-emptively.

<blockquote>
I was at an event where two people later tested positive for Coronavirus... There is a limited amount of tests available and there are people who need tests more than I do, especially when I wasn't showing any symptoms at all. So what I've done is keep myself isolated this past week.<br>
<cite>
<a href="https://twitter.com/LewisHamilton/status/1241294407942516736/photo/1">Lewis Hamilton</a>
</cite>
</blockquote>

[subclinical]: https://en.wikipedia.org/wiki/Subclinical_infection

### kill the virus

{no eradication without vaccination}

### don't wait and see

### don't jump the gun


## conclusions

**WARNING:** The author is not a medical expert.
These conclusions are neither proven nor peer-reviewed.

- COVID-19 moves fast. Timing is critically important.
- Infectious people should be quarantined **immediately**.
- Self-quarantine *after* symptoms become obvious is good, but too slow.
- People who become immune (if that's possible) should be un-quarantined.
- When symptoms are subtle, accurate timing requires broad access to testing.
