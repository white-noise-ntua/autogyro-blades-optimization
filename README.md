# Black-Box Optimization of Autogyro Blade's Shape

Our team participates in [CanSat Competition 2019](http://www.cansatcompetition.com/) and has to develop a CanSat that
will descent without a parachute, using only freely spining
blades ([autogyro descent](https://en.wikipedia.org/wiki/Autogyro)). We used a simulation (provided to us by NTUA's
Fluid Mechanics Department) that takes as input the blade's
chord and twist at different values of the radius and computes
the angular momentum at the equilibrium point as well as the
terminal velocity of our CanSat.

In order to make our control system's job easier we want to
design a blade that minimizes the angular momentum of the
rotor so as to constrain the gyroscopic effects. To achieve
that we did the following:

### 1. Blade Parametrization

The blade is characterized by 2 functions associating chord
with radius and twist with radius. We modeled the chord-radius
and twist-radius functions as [__Bezier Curves__](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) with 4 and 3
control points respectively. Therefore, we are able to
__uniquely determine a blade using only 7 variables:__

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\overrightarrow{x}&space;=&space;[c_1,&space;c_2,&space;c_3,&space;c_4,&space;t_1,&space;t_2,&space;t_3]" title="\overrightarrow{x} = [c_1, c_2, c_3, c_4, t_1, t_2, t_3]" />

### 2. Cost Function

The angular velocity <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\omega(\overrightarrow{x})" title="\omega(\overrightarrow{x})" /> and terminal descent rate <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;v(\overrightarrow{x})" title="v(\overrightarrow{x})" /> computed from
the simulation are a function of our state vector  <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\overrightarrow{x}" title="\overrightarrow{x}" />.

We want the minimum angular velocity and a terminal velocity
in the range [11,14] m/s, so the cost function will look as following:

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;L(\overrightarrow{x})&space;=&space;I&space;(\overrightarrow{x})\cdot\omega(\overrightarrow{x})&space;&plus;&space;f(v(\overrightarrow{x}))" title="L(\overrightarrow{x}) = I(\overrightarrow{x}) \omega(\overrightarrow{x}) + f(v(\overrightarrow{x}))" />

(Please note that all of the above functions have values in
  the real numbers.)

Where f is a function that has nearly zero values in the
region of interest ( [11,14] ) and grows exponentially outside
this region.For the function f we used:

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;f(y)&space;=&space;1000&space;\cdot&space;e^{\frac{-40}{(y-12)^2}}" title="f(x) = 1000 \cdot e^{\frac{-40}{(x-12)^2}}" />

![](Figure_1.png)

### 3. Projected Gradient Descent

In order to determine the desired blade, we have to find the state vector <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\overrightarrow{x}" title="\overrightarrow{x}" /> that minimizes our cost function <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;L(\overrightarrow{x})" title="\overrightarrow{x}" /> :

<img src="https://latex.codecogs.com/png.latex?x^{*}&space;=&space;\underset{\overrightarrow{x}&space;\in&space;\mathbb{R}^7}{argmin}&space;L(\overrightarrow{x})" title="x^{*} = \underset{\overrightarrow{x} \in \mathbb{R}^7}{argmin} L(\overrightarrow{x})" />

In real life, there are some manufacturing constraints for the blade so the accepted state vectors must lie in a set, let <img src="https://latex.codecogs.com/png.latex?S" title="S" /> , that is the set of all blades with certain characteristics.

To minimize the function <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;L(\overrightarrow{x})" title="\overrightarrow{x}" /> over <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\overrightarrow{x}\in&space;S" title="\overrightarrow{x}\in S" /> we will use the Projected
Gradient Descent Algorithm. Starting from a blade with state vector <img src="https://latex.codecogs.com/gif.latex?\dpi{100}&space;\overrightarrow{x}_{0}" title="\overrightarrow{x}_{0}" /> we are using the following update law to iterratively improve our blade:

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\overrightarrow{x}_{i&plus;1}&space;=&space;\underset{S}{proj}\left(\overrightarrow{x}_{i}&space;-&space;\eta&space;\cdot&space;\nabla&space;L(\overrightarrow{x}_{i})&space;\right)" title="\overrightarrow{x}_{i+1} = \underset{S}{proj}\left(\overrightarrow{x}_{i} - \eta \cdot \nabla L(\overrightarrow{x}_{i}) \right)" />

Where <img src="https://latex.codecogs.com/png.latex?\eta" title="\eta" /> is a positive constant.

The partial derivatives are calculated as:

<img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\frac{\partial&space;L([x_1,\dots,x_i,\dots,x_7])}{\partial&space;x_i}&space;=&space;\frac{L([x_1,\dots,x_i&space;&plus;&space;\epsilon,\dots,x_7])&space;-&space;L([x_1,\dots,x_i,\dots,x_7])}{\epsilon}" title="\frac{\partial L([x_1,\dots,x_i,\dots,x_7])}{\partial x_i} = \frac{L([x_1,\dots,x_i + \epsilon,\dots,x_7]) - L([x_1,\dots,x_i,\dots,x_7])}{\epsilon}" />

Which can also be written as:

<img src="https://latex.codecogs.com/png.latex?\dpi{150}&space;\frac{\partial&space;L(\overrightarrow{x})}{\partial&space;x_i}&space;=&space;\frac{L(\overrightarrow{x}&plus;\epsilon&space;\cdot&space;\overrightarrow{\delta_i}))&space;-&space;L(\overrightarrow{x})}{\epsilon}" title="\frac{\partial L(\overrightarrow{x})}{\partial x_i} = \frac{L(\overrightarrow{x}+\epsilon \cdot \overrightarrow{\delta_i})) - L(\overrightarrow{x})}{\epsilon}" />
