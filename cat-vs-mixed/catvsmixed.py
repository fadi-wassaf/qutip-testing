import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from qutip import *

N = 20
a = 3
xyvec = np.linspace(-6,6,100)
xgrid, ygrid = np.meshgrid(xyvec, xyvec)

# States to plot
cat_state_2 = coherent(N, a) + coherent(N, -a)
cat_state_3 = coherent(N, a) + coherent(N, np.exp(2j*np.pi/3)*a) + coherent(N, np.exp(4j*np.pi/3)*a)
cat_state_4 = coherent(N, a) + coherent(N, 1j*a) + coherent(N, -a) + coherent(N, -1j*a)
mixed_state_2 = coherent_dm(N, a) + coherent_dm(N, -a)
mixed_state_3 = coherent_dm(N, a) + coherent_dm(N, np.exp(2j*np.pi/3)*a) + coherent_dm(N, np.exp(4j*np.pi/3)*a)
mixed_state_4 = coherent_dm(N, a) + coherent_dm(N, -a) + coherent_dm(N, 1j*a) + coherent_dm(N, -1j*a)
states = [cat_state_2, cat_state_3, cat_state_4, mixed_state_2, mixed_state_3, mixed_state_4]

# Generate 2D plots for all the states
for i, state in enumerate(states):
    fig, ax = plt.subplots()
    wig = wigner(state, xyvec, xyvec)
    wlim = abs(wig).max()
    ax.contourf(xyvec, xyvec, wig, 100, cmap='RdBu', norm=mpl.colors.Normalize(-wlim, wlim))
    plt.savefig('2d%d' % i, dpi=300)

# Generate 3D plots for all the states
for i, state in enumerate(states):
    fig = plt.figure()
    ax = Axes3D(fig)
    wig = wigner(state, xyvec, xyvec)
    ax.plot_surface(xgrid, ygrid, wig, cmap='Blues')
    plt.savefig('3d%d' % i, dpi=300)