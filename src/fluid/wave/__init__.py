"""Water wave mechanics.

Usage:
    from fluidpy import wave
    k = wave.wavenumber(T=8.0, d=16.0)
"""
from .constants import G, RHO_WATER
from .linear import (
    solve_wavenumber, wavelength, phase_speed, group_velocity,
    surface_elevation, velocity_field, particle_orbit, pressure,
)
from .regimes import classify_depth
from .energy import (
    potential_energy, kinetic_energy, total_energy, energy_flux,
)
from .shoaling import shoal, shoaling_coefficient
from .stokes import stokes2_elevation, stokes2_velocity, fenton5
from . import plotting

__all__ = [
    "G", "RHO_WATER",
    "solve_wavenumber", "wavelength", "phase_speed", "group_velocity",
    "surface_elevation", "velocity_field", "particle_orbit", "pressure",
    "classify_depth",
    "potential_energy", "kinetic_energy", "total_energy", "energy_flux",
    "shoal", "shoaling_coefficient",
    "stokes2_elevation", "stokes2_velocity", "fenton5",
    "plotting",
]
