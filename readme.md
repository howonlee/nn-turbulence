Suspiciously turbulence-ish phenomena in neural net
===

I was looking at renormalization group stuff for [Mertonon](https://github.com/howonlee/mertonon) in preparation for implementations like... 6 months from now... when I decided I would poke at things while being weird about the grid sample.

Peeps poke at neural net for [turbulence modeling](https://pubs.aip.org/aip/pof/article-abstract/34/2/025111/2847083/Attention-enhanced-neural-network-models-for?redirectedFrom=fulltext) but that's not what we're dealing with. If you 'sweep' an unfitted neural net over 2 dimensions of its high-dimensional input space and read out from an output neuron, you get what seems to be a turbulence phenomenon. I haven't tested fitted net because I am lazy and all I wanted to do was look at the turbulent nature of the thing.

But who cares, look at pretty pictures. I do understand the nonlinearity in the actual given image (from arbitrary runs of the included python file `grid_sweep.py`) is this deranged thing, switch it out for the included vaguely normal one if you're feeling it and see what you get.

<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig1.png" width="480" height="360">
<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig2.png" width="480" height="360">
<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig3.png" width="480" height="360">

I don't have, like a [Kolmogorov power spectrum yadda yadda 5/3 yadda yadda](https://spie.org/samples/FG02.pdf) something something that [poem about the fleas](https://en.wikipedia.org/wiki/Siphonaptera_(poem)) but it sure looks like turbulence to me, basically
