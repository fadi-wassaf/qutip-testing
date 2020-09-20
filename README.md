# qutip-testing
Some random tests and visualizations that I've done in QuTiP while studying.

## Quantum Harmonic Oscillator Transition n=0 to n=3

Wigner function plots of the excitation due to the perturbation applied:
<i>|<i>
:---------------:|:---------------:
![qho_wig_2d](./qho-transition/anim2d.gif)|![qho_wig_3d](./qho-transition/anim3d.gif)

</br>

## Wigner functions of Cat States and Mixed States of the Coherent State

For the coherent state

![coherent](https://latex.codecogs.com/svg.latex?\left|%20\alpha%20\right%3E%20=%20e^{-\frac{1}{2}|\alpha|^2}\sum_{n=0}^{\infty}\frac{\alpha^n}{\sqrt{n!}}\left|n\right%3E)

I plotted the Wigner function for the following cat and mixed states for alpha=3:

#### Cat states

![cat2](https://latex.codecogs.com/svg.latex?\left|\psi\right%3E%20=%20\left|\alpha\right%3E%20+%20\left|-\alpha\right%3E)

<i>|<i>
:---------------:|:---------------:
![cat2_2d](./cat-vs-mixed/2d0.png)|![cat2_3d](./cat-vs-mixed/3d0.png)

</br>

![cat3](https://latex.codecogs.com/svg.latex?\left|\psi\right%3E%20=%20\left|\alpha\right%3E%20+%20\left|e^{i2\pi/3}\alpha\right%3E%20+%20\left|e^{i4\pi/3}\alpha\right%3E)
<i>|<i>
:---------------:|:---------------:
![cat3_2d](./cat-vs-mixed/2d1.png)|![cat3_3d](./cat-vs-mixed/3d1.png)

</br>

![cat4](https://latex.codecogs.com/svg.latex?\left|\psi\right%3E%20=%20\left|\alpha\right%3E%20+%20\left|-\alpha\right%3E%20%20+%20\left|i\alpha\right%3E%20+%20\left|-i\alpha\right%3E)

<i>|<i>
:---------------:|:---------------:
![cat4_2d](./cat-vs-mixed/2d2.png)|![cat4_3d](./cat-vs-mixed/3d2.png)

</br>

![mixed2](https://latex.codecogs.com/svg.latex?\hat\rho%20=%20\left|\alpha\right%3E\left%3C\alpha\right|%20+%20\left|-\alpha\right%3E\left%3C-\alpha\right|)

<i>|<i>
:---------------:|:---------------:
![mixed2_2d](./cat-vs-mixed/2d3.png)|![mixed2_3d](./cat-vs-mixed/3d3.png)

</br>

![mixed3](https://latex.codecogs.com/svg.latex?\hat\rho%20=%20\left|\alpha\right%3E\left%3C\alpha\right|%20+%20\left|e^{i2\pi/3}\alpha\right%3E\left%3Ce^{i2\pi/3}\alpha\right|%20+%20\left|e^{i4\pi/3}\alpha\right%3E\left%3Ce^{i4\pi/3}\alpha\right|)
<i>|<i>
:---------------:|:---------------:
![mixed3_2d](./cat-vs-mixed/2d4.png)|![mixed3_3d](./cat-vs-mixed/3d4.png)

</br>

![mixed4](https://latex.codecogs.com/svg.latex?\hat\rho%20=%20\left|\alpha\right%3E\left%3C\alpha\right|%20+%20\left|-\alpha\right%3E\left%3C-\alpha\right|%20+%20\left|i\alpha\right%3E\left%3Ci\alpha\right|+%20\left|-i\alpha\right%3E\left%3C-i\alpha\right|)
<i>|<i>
:---------------:|:---------------:
![mixed4_2d](./cat-vs-mixed/2d5.png)|![mixed4_3d](./cat-vs-mixed/3d5.png)
