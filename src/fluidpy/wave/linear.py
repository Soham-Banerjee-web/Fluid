"""Linear regular wave theory (Small Amplitude Wave Theory), lecture section 2.

Sign/axis convention: z = 0 at still water level, z = -d at the bed,
eta = a sin(omega t - k x).
"""
from __future__ import annotations


def solve_wavenumber(T, d, g=9.81):
    """Solve the dispersion equation omega^2 = g k tanh(k d) for k (eq 2.14).

    Implicit, so solved iteratively (e.g. Newton-Raphson).
    """
    raise NotImplementedError


def wavelength(T, d, g=9.81):
    """lambda = 2 pi / k."""
    raise NotImplementedError


def phase_speed(T, d, g=9.81):
    """c = omega / k = [(g/k) tanh(kd)]^(1/2) (eq 2.13)."""
    raise NotImplementedError


def group_velocity(T, d, g=9.81):
    """cg = (c/2) [1 + 2kd / sinh(2kd)] (eq 4.4)."""
    raise NotImplementedError


def surface_elevation(a, k, omega, x, t):
    """eta = a sin(omega t - k x) (eq 2.10)."""
    raise NotImplementedError


def velocity_field(a, k, omega, d, x, z, t):
    """Horizontal and vertical velocity (u, w) from eq 2.9."""
    raise NotImplementedError


def particle_orbit(a, k, omega, d, x, z, t):
    """Fluid particle displacement (xi, eta_hat) from eq 2.11."""
    raise NotImplementedError


def pressure(a, k, omega, d, x, z, t, rho=1025.0, g=9.81, p0=0.0):
    """Total pressure p = p0 - rho g z + rho g a cosh[k(z+d)]/cosh(kd) sin(omega t - k x) (eq 2.15)."""
    raise NotImplementedError
