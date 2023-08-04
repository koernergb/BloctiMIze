import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light in m/s
h = 6.62e-34  # Planck's constant in J*s

# Simulation parameters
cutoff = 1e12  # Reduce frequency cutoff to 1 THz
N = 1000  # Reduce number of samples
dx = 10e-6  # Spatial resolution of 10 micrometers

# Frequency spacing
df = cutoff / N

# Frequency values
freqs = np.arange(0, cutoff, df)

# Wavevector magnitudes
ks = 2 * np.pi * freqs / c

# Random phases
phases = 2 * np.pi * np.random.rand(N)

# Electric field amplitude
E0 = (h * freqs)**0.5

# Generate random 3D E-field
Ex = E0 * np.cos(phases) * np.random.randn(N)
Ey = E0 * np.sin(phases) * np.random.randn(N)
Ez = E0 * np.cos(0.5 * phases) * np.random.randn(N)

# Magnetic field amplitude
B0 = E0 / c

# Generate random 3D B-field
Bx = B0 * np.sin(phases) * np.random.randn(N)
By = B0 * np.cos(phases) * np.random.randn(N)
Bz = B0 * np.sin(0.5 * phases) * np.random.randn(N)

# Position arrays
x = np.arange(0, 0.002, dx)  # Simulate 2 mm region
y = np.arange(0, 0.002, dx)
z = np.arange(0, 0.002, dx)

# Create meshgrid
X, Y, Z = np.meshgrid(x, y, z)

# Evaluate electric field
Exyz = np.zeros_like(X)
for i in range(N):
    Exyz += np.sin(ks[i] * X + phases[i]) * Ex[i]
    Exyz += np.sin(ks[i] * Y + 0.5 * phases[i]) * Ey[i]
    Exyz += np.sin(ks[i] * Z + 0.25 * phases[i]) * Ez[i]

# Evaluate magnetic field
Bxyz = np.zeros_like(X)
for i in range(N):
    Bxyz += np.sin(ks[i] * X + phases[i]) * Bx[i]
    Bxyz += np.sin(ks[i] * Y + 0.5 * phases[i]) * By[i]
    Bxyz += np.sin(ks[i] * Z + 0.25 * phases[i]) * Bz[i]

# Spatial field energy density
energy_density = Exyz**2 + Bxyz**2  # Adding permeability (assume 1 for simplicity)

# Visualization
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, energy_density)
ax.set_title('Spatial Energy Density Distribution')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

plt.show()
