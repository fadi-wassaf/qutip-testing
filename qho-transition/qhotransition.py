import matplotlib as mpl
mpl.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import time
from qutip import *

N = 4             # Hilbert Space Levels
a = destroy(N)    # Annihilation operator
c = a.dag()       # Creation operator

# Decaying Perturbation Coefficient
def V_pert(t, args):
    return np.exp((-t)**2)

init_state = basis(N, 0)

# Hamiltonian Setup - Simple QHO H0 plus perturbation
H0 = c * a        
H = [H0, [c*c*c, V_pert]]

# Solve for states at different times
times = np.linspace(0, 3, 150)
output = mesolve(H, init_state, times)

# Get Wigner function for each state at the different times
xyvec = np.linspace(-6,6,300)
xgrid, ygrid = np.meshgrid(xyvec, xyvec)
wigner_fns = [s for s in output.states]

# Update function to make animation
def plot_func(n, ax1, type, ax2):
    ax1.cla()
    if ax2 != None: ax2.cla()
    # Plot Wigner function of the state at the current time
    curr_state = wigner_fns[n]
    wig = wigner(curr_state, xyvec, xyvec)
    if type == '3d':
        ax1.plot_surface(xgrid, ygrid, wig, cmap='Blues')
    if type == '2d':
        wlim = abs(wig).max()
        ax1.contourf(xyvec, xyvec, wig, 100, cmap='RdBu', norm=mpl.colors.Normalize(-wlim, wlim))
    if type == 'both':
        wlim = abs(wig).max()
        ax1.contourf(xyvec, xyvec, wig, 100, cmap='RdBu', norm=mpl.colors.Normalize(-wlim, wlim))
        ax2.plot_surface(xgrid, ygrid, wig, cmap='Blues')

# Create animation for 3D plot
fig = plt.figure()
ax = Axes3D(fig, azim=-14, elev=21)
anim = animation.FuncAnimation(fig, plot_func, frames=len(wigner_fns), fargs=[ax, '3d', None])
anim.save('anim3d.mp4', fps=30, dpi=300, progress_callback=lambda i, n : print('\r3d Frame %d/%d' % (i+1, n), end=''))
print()

# Create animation for 2D plot
fig, ax = plt.subplots()
anim = animation.FuncAnimation(fig, plot_func, frames=len(wigner_fns), fargs=[ax, '2d', None])
anim.save('anim2d.mp4', fps=30, dpi=300, progress_callback=lambda i, n : print('\r2d Frame %d/%d' % (i+1, n), end=''))
print()

# Create combined animation
fig = plt.figure(figsize=(17,8))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.view_init(azim=-14, elev=21)
anim = animation.FuncAnimation(fig, plot_func, frames=len(wigner_fns), fargs=[ax1, 'both', ax2])
anim.save('animcombined.mp4', fps=30, dpi=300, progress_callback=lambda i, n : print('\rCombined Frame %d/%d' % (i+1, n), end=''))
print()


