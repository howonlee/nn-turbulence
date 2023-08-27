Wibbley wobbley pictures with neural nets
===

I was looking at renormalization group stuff for [Mertonon](https://github.com/howonlee/mertonon) in preparation for implementations like... 6 months from now... when I decided I would poke at things while being weird about the latent space.

Peeps poke at neural net for [turbulence modeling](https://pubs.aip.org/aip/pof/article-abstract/34/2/025111/2847083/Attention-enhanced-neural-network-models-for?redirectedFrom=fulltext) but that's not what we're dealing with. There is of course also a chaotician's point of view on net, diffusion in latent space, etc etc. But this way is way dumber and funner, even compared to just the ol' linear interpolation of data points through latent space, which only really has meaning in fitted net.

If you 'sweep' an unfitted neural net over 2 dimensions of its high-dimensional input space and read out from an output neuron, you get what seems to be sometimes a turbulent, sometimes a laminar phenomenon. I haven't tested fitted net because I am lazy and all I wanted to do was look at the thing.

But who cares, look at pretty pictures. I do understand the nonlinearity in the actual given images (from arbitrary runs of the included python file `grid_sweep.py`) is this deranged norm thing, switch it out for the included vaguely normal one if you're feeling it and see what you get.

<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig1.png" width="480" height="360">
<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig2.png" width="480" height="360">
<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig3.png" width="480" height="360">

I don't have, like a [Kolmogorov power spectrum yadda yadda 5/3 yadda yadda](https://spie.org/samples/FG02.pdf) something something that [poem about the fleas](https://en.wikipedia.org/wiki/Siphonaptera_(poem)) but it sure looks like turbulence snapshots to me, from the results of mark 1 eyeball. And here's some more boring laminar-looking ones, from tanh nonlinearity.

<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig4.png" width="480" height="360">
<img src="https://raw.githubusercontent.com/howonlee/nn-turbulence/master/fig5.png" width="480" height="360">
