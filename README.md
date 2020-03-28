# contagion window models

## UNDER CONSTRUCTION


## abstract

Contagion window models simulate [viral phenomena] with time-dependent [transmission] probabilities. Discrete models use [recurrence relations], not differential equations, for computational simplicity.

A discrete [window] is a sequence **w** such that each element <i>w<sub>i</sub></i> is the expected number of transmissions from one node after *i* days of infection. Like 𝛽 in a [SIR model], window elements represent averaged behavior of many individual nodes. Quarantine after *q* days of infection can be modeled by setting <i>w<sub>i</sub></i> = 0 for all *i* &ge; *q*. [Social distancing] and/or reduced transmission probability can be modeled by decreasing window magnitude |**w**|.

The examples shown here use [finite-response] windows with fixed duration. Each node is assumed to die or become permanently immune after 𝜏 days. The infection duration 𝜏 must be estimated experimentally.

THE EXAMPLES HERE ARE NOT MEDICAL ADVICE. The author is a physicist, not an epidemiologist.

[viral phenomena]: https://en.wikipedia.org/wiki/Viral_phenomenon
[transmission]: https://en.wikipedia.org/wiki/Transmission_(medicine)
[recurrence relations]: https://en.wikipedia.org/wiki/Recurrence_relation
[window]: https://en.wikipedia.org/wiki/Window_function
[SIR model]: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
[Social distancing]: https://en.wikipedia.org/wiki/Social_distancing
[finite-response]: https://en.wikipedia.org/wiki/Finite_impulse_response


## contents


## definitions

See this [Jupyter] notebook for definitions and equations: [books/model.ipynb]

[Jupyter]: https://jupyter.org/
[books/model.ipynb]: books/model.ipynb


## examples

### count the days

{natural window with citations}

### flatten the curve

{reduce |**w**| by decreasing contact frequency}

<blockquote>
We need to take the first step: returning. It's not even going to God. No! It's simply returning home.
<br>
<cite>
<a href="https://www.youtube.com/watch?v=IlbXjPE55Fc">
Pope Francis</a>
</cite>
</blockquote>

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

{herd immunity from widespread vaccination}

<blockquote>
There is no patent. Could you patent the sun?<br>
<cite>
<a href="https://en.wikiquote.org/wiki/Jonas_Salk">
Jonas Salk</a>
</cite>
</blockquote>

### don't wait and see

### don't jump the start



